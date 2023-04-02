import os.path
import sys

from DatasetBase import DatasetBase


class DatasetLJSpeech(DatasetBase):

    def export_dataset(self, path=None):
        pass

    def get_readable_name(self):
        return 'ljspeech'

    def print_type_help(self):
        print("Type:", self.get_readable_name)
        print(" Datatype in LJSpeech-Format")
        print(" See https://keithito.com/LJ-Speech-Dataset/ for a description of the type")
        print(" You must provide the full path to the metadata-file as additional file parameter (-if or -of)")

    def import_dataset(self, path=None):
        if path is None or not os.path.exists(path):
            sys.exit("Error: You must provide a valid path for dataset.")
