import json
import os.path
import sys

from DatasetBase import DatasetBase

class DatasetTabFilter(DatasetBase):

    def export_dataset(self, path=None):
       sys.exit("Error: Dataset "+self.get_readable_name()+" only supports import")

    def get_readable_name(self):
        return 'tabfilter'

    def print_type_help(self):
        print("Type:", self.get_readable_name())
        print(" Datatype in Tabulator Format with Import filtering")
        print(" ATTENTION: This Datatype only supports import, no export.")
        print(" Description how to use: https://github.com/fungus75/wdsutil/wiki/tabfilter")
        print(" You must provide the filter-config as additional file parameter (-if)")

    def import_dataset(self, path=None):
        if path is None or not os.path.exists(path):
            sys.exit("Error: You must provide a filter-config file as additional parameter.")

        self.index_cache={}

        # load config
        with open(path) as file:
            try:
                self.filterconfig = json.load(file)
            except Exception:
                sys.exit("Error loading filter-config")
            file.close()

        self.validate_config(["tabfile", "hasHeader", "encoding", "fields", "audioformat", "basepathwave",
                              "adjustaudiofilename", "wave_convert_command", "includeprotocol"])

        if not os.path.exists(self.filterconfig["tabfile"]):
            sys.exit("Error: tabfile "+self.filterconfig["tabfile"]+ " not found")

        includeprotocol = open(self.filterconfig["includeprotocol"], "w", encoding=self.filterconfig["encoding"])


        with open(self.filterconfig["tabfile"], "r", encoding=self.filterconfig["encoding"]) as tabfile:
            if self.filterconfig["hasHeader"]:
                # read first line as header-line
                headerstring = tabfile.readline().strip()
                self.tabfile_headers = headerstring.split("\t")
            else:
                if "header" not in self.filterconfig:
                    sys.exit("Error: Missing Parameter in filter-config: header")
                self.tabfile_headers = self.filterconfig["header"]

            # write header to includeprotocol
            includeprotocol.write("\t".join(self.tabfile_headers))
            includeprotocol.write("\n")

            # read datalines
            for line in tabfile:
                lineelements=line.strip().split("\t")

                if not self.filtermatched(lineelements):
                    continue

                includeprotocol.write("\t".join(lineelements))
                includeprotocol.write("\n")

                filename = self.eval_filename(self.get_corresponding_field(lineelements, "audiofile"))
                filename = self.convert_wave_format(filename)
                if not os.path.exists(filename):
                    print(" > Warning: wav-file missing: " + filename)
                    if self.mainConfig['flexible']:
                        continue
                    raise FileNotFoundError(filename)

                text = self.get_corresponding_field(lineelements, "text")
                region = self.get_corresponding_field(lineelements, "region")
                age = self.get_corresponding_field(lineelements, "age")
                gender = self.get_corresponding_field(lineelements, "sex")

                age = self.try_conversion(age, "age")
                gender = self.try_conversion(gender, "sex")

                self._add_content_line(fullPathWaveFile=filename,
                                       text=text,
                                       region=region,
                                       age=age,
                                       gender=gender)

            tabfile.close()
        includeprotocol.close()
        return self._getContent()

    def get_corresponding_field(self, elements, field):
        if field not in self.filterconfig["fields"]:
            return None
        tabfield = self.filterconfig["fields"][field]
        return self.get_field(elements, tabfield)

    def get_field(self, elements, field):
        index = self.get_index_for_field(field)
        return elements[index]

    def get_index_for_field(self, field):
        if field not in self.index_cache:
            self.index_cache[field] = self.tabfile_headers.index(field)

        # return from cache
        return self.index_cache[field]

    def validate_config(self, params):
        for param in params:
            if param not in self.filterconfig:
                sys.exit("Error: Missing Parameter in filter-config: "+ param)

    def convert_filename(self, filename):
        if self.filterconfig["adjustaudiofilename"] == "keep":
            return filename

        if self.filterconfig["adjustaudiofilename"] == "replaceExtension":
            lastdot=filename.rfind(".")
            if lastdot == -1:
                return filename+"."+self.filterconfig["audioformat"]
            return filename[:lastdot]+"."+self.filterconfig["audioformat"]

        sys.exit("Error: Unknown adjustaudiofilename: " + self.filterconfig["adjustaudiofilename"])

    def eval_filename(self, filename):
        if filename is None:
            sys.exit("Error: Filename is None")
        filename = self.convert_filename(filename)
        return os.path.join(self.filterconfig["basepathwave"], filename)

    def convert_wave_format(self, filename):
        if self.filterconfig["audioformat"] == "wav":
            return filename

        # convert fileformat
        lastdot = filename.rfind(".")
        newfilename=filename[:lastdot] + ".wav"
        if os.path.exists(newfilename):
            return newfilename

        command = self.filterconfig["wave_convert_command"].format(
            origfilename=filename,
            wavefilename=newfilename
        )
        print(command)
        os.system(command)

        return newfilename

    def try_conversion(self, value, name):
        if "conversion" not in self.filterconfig or name not in self.filterconfig["conversion"]:
            # no conversion defined
            return value

        if value not in self.filterconfig["conversion"][name]:
            # no matching value found
            return value

        # return conversion
        return self.filterconfig["conversion"][name][value]

    def filtermatched(self, elements):
        if "filter" not in self.filterconfig:
            return True

        if "and" in self.filterconfig["filter"]:
            for andfield in self.filterconfig["filter"]["and"]:
                value = self.filterconfig["filter"]["and"][andfield]
                if self.get_field(elements,andfield) != value:
                    # each field must pass, otherwise return false
                    return False

        if "or" in self.filterconfig["filter"]:
            for orfield in self.filterconfig["filter"]["or"]:
                value = self.filterconfig["filter"]["or"][orfield]
                if self.get_field(elements,orfield) == value:
                    # each field must pass, otherwise return false
                    return True
            # no matching or field found
            return False

        # all filters matched
        return True






