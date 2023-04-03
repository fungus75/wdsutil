import sys


class DsFabric:
    datatype_dict = {}
    mainConfig = None

    def __init__(self, mainConfig):
        self.mainConfig=mainConfig

    def register_datatype(self, datatype=None):
        if datatype is not None:
            idx = datatype.get_readable_name()
            self.datatype_dict[idx] = datatype

    def get_types_as_list(self):
        ret = ""
        for dt in self.datatype_dict.values():
            if ret != "":
                ret += ", "
            ret += dt.get_readable_name()
        return ret

    def type_help(self):
        for dt in self.datatype_dict.values():
            dt.print_type_help()
            print()

    def get(self, dataset_type):
        if not dataset_type in self.datatype_dict:
            sys.exit("Error: unknown type "+dataset_type+", please try -th parameter")
        return self.datatype_dict[dataset_type]
