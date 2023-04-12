import abc

from DsContent import DsContent


class FilterBase:
    __metaclass__ = abc.ABCMeta

    new_content = None

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
    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):
        """Returns info about the dataset"""

    def _add_content_item(self, item, include):
        """Adds a content-line to the new content, if include is set to True, otherwise not
        and takes care of the not_filter_flag which turns around the include-parameter-behaviour"""

        if self.mainConfig["not_filter_flag"]:
            include = not include

        if self.new_content is None:
            self.new_content = DsContent(self.mainConfig)

        if include:
            self.new_content.add_item(item)
