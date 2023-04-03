import abc
import os

from DsContent import DsContent


class DatasetBase:
    __metaclass__ = abc.ABCMeta

    # Entries
    entry_list = []
    mainConfig = None
    content = None

    def __init__(self, mainConfig):
        self.mainConfig = mainConfig
        self.content = DsContent(self.mainConfig)

    @abc.abstractmethod
    def get_readable_name(self):
        """returns a human-readable name of the dataset-type"""
        return

    @abc.abstractmethod
    def import_dataset(self, path=None):
        return

    @abc.abstractmethod
    def export_dataset(self, path=None):
        return

    @abc.abstractmethod
    def print_type_help(self):
        """Prints out some information about the type"""

    def _add_content_line(self,
                          relativeWaveFile=None,
                          relativeWaveFileNoExtension=None,
                          fullPathWaveFile=None,
                          basisPathWaveFile=None,
                          text=None,
                          lowerText=None,
                          upperText=None
                          ):
        item = self.content.item_generator(relativeWaveFile,relativeWaveFileNoExtension,
                                           fullPathWaveFile,basisPathWaveFile,
                                           text,lowerText,upperText)

        # validate filename
        if not os.path.exists(item['fullPathWaveFile']) and not self.mainConfig['flexible']:
            raise Exception("Wave File " + fullPathWaveFile + " not found/not accessible")

        if not os.path.exists(item['fullPathWaveFile']):
            return

        self.content.add_item(item)

    def _getContent(self):
        return self.content
