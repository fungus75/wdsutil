import os.path
import shutil
import sys

from DatasetBase import DatasetBase


class DatasetFilePairs(DatasetBase):

    def export_dataset(self, path=None):
        if path is None:
            sys.exit("Error: You must provide a valid path for exporting dataset.")

        basisPathWaveFile = path
        if os.path.exists(path) and self.mainConfig['overwrite']:
            os.remove(path)
            if os.path.exists(basisPathWaveFile):
                shutil.rmtree(basisPathWaveFile)
        if os.path.exists(path):
            sys.exit("Error: Export path exist, please provide an non-existing path!")

        if not os.path.exists(basisPathWaveFile):
            os.makedirs(basisPathWaveFile)

        if not os.path.isdir(basisPathWaveFile):
            sys.exit("Error: This is not a directory: "+basisPathWaveFile)


        for i in range(0, self.content.size()):
            item = self.content.get(i)
            shutil.copyfile(item['fullPathWaveFile'],
                            os.path.join(basisPathWaveFile, item['relativeWaveFile']))
            metafile = open(os.path.join(basisPathWaveFile, item['relativeWaveFileNoExtension']+".txt"),
                            'w',
                            encoding="utf-8")
            metafile.write(item['text'] )
            metafile.close()

    def get_readable_name(self):
        return 'filepairs'

    def print_type_help(self):
        print("Type:", self.get_readable_name())
        print(" Datatype in File Pairs-Format")
        print(" (Each Wave-file has a corresponding text file, i.E. 1.wav and 1.txt)")
        print(" You must provide the full path to the folder containing wav and txt files " +
              "as additional file parameter (-if or -of)")

    def import_dataset(self, path=None):
        if path is None or not os.path.exists(path) or not os.path.isdir(path):
            sys.exit("Error: You must provide a valid path for dataset.")

        basisPathWaveFile = path
        for filename in os.listdir(basisPathWaveFile):
            if not filename.lower().endswith(".txt"):
                # only .txt are interesting at the moment.
                continue
            basisfilename = filename[0:-4]
            if not os.path.exists(os.path.join(basisPathWaveFile, basisfilename+".wav")):
                print(" > Warning: wav-file missing for "+filename)
                if self.mainConfig['flexible']:
                    continue
                raise FileNotFoundError(basisfilename+".wav")

            metafile = open(os.path.join(basisPathWaveFile, filename), 'r', encoding="utf-8")
            text = " ".join(metafile.readlines()).strip()
            lowerText=text.lower()
            self._add_content_line(relativeWaveFileNoExtension=basisfilename,
                                   basisPathWaveFile=basisPathWaveFile,
                                   text=text,
                                   lowerText=lowerText)
            metafile.close()
        return self._getContent()
