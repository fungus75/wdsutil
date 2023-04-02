import abc


class DatasetBase:
    __metaclass__ = abc.ABCMeta

    # Entries
    entry_list = []

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
