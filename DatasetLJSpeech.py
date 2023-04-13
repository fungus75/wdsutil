import os.path
import shutil
import sys

from DatasetBase import DatasetBase


class DatasetLJSpeech(DatasetBase):

    def export_dataset(self, path=None):
        if path is None:
            sys.exit("Error: You must provide a valid path for exporting dataset.")

        basisPathWaveFile = self._eval_wave_path(path)
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

        metafile = open(path, 'w')
        for i in range(0, self.content.size()):
            item = self.content.get(i)
            shutil.copyfile(item['fullPathWaveFile'],
                            os.path.join(basisPathWaveFile, item['relativeWaveFile']))
            metafile.write(item['relativeWaveFileNoExtension'] + '|' +
                           item['text'] + '|' +
                           item['lowerText'])
        metafile.close()

    def get_readable_name(self):
        return 'ljspeech'

    def print_type_help(self):
        print("Type:", self.get_readable_name())
        print(" Datatype in LJSpeech-Format")
        print(" See https://keithito.com/LJ-Speech-Dataset/ for a description of the type")
        print(" You must provide the full path to the metadata-file as additional file parameter (-if or -of)")

    def _eval_wave_path(self, path=None):
        return os.path.join(os.path.dirname(path), "wavs")

    def import_dataset(self, path=None):
        if path is None or not os.path.exists(path):
            sys.exit("Error: You must provide a valid path for dataset.")

        basisPathWaveFile = self._eval_wave_path(path)
        metafile = open(path, 'r')
        for line in metafile:
            parts = line.split('|')
            lowerText=None
            if len(parts)>2:
                lowerText=parts[2]
            self._add_content_line(relativeWaveFileNoExtension=parts[0],
                                   basisPathWaveFile=basisPathWaveFile,
                                   text=parts[1],
                                   lowerText=lowerText)
        metafile.close()
        return self._getContent()
