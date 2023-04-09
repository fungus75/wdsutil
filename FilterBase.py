import abc


class FilterBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self, mainConfig):
        self.mainConfig = mainConfig

    @abc.abstractmethod
    def get_readable_name(self):
        """returns a human-readable name of the dataset-type"""
        return

    @abc.abstractmethod
    def print_filter_help(self):
        """Prints out some information about the type"""

    @abc.abstractmethod
    def perform(self, ds_content):
        """Returns info about the dataset"""
