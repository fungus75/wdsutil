import abc

from DsContent import DsContent
from FilterBase import FilterBase


class FilterAll(FilterBase):
    def get_readable_name(self):
        return "all"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" filter all, means copy any dataset to destination")


    def perform(self, ds_content):
        if self.mainConfig["not_filter_flag"]:
            ds_content =  DsContent(self.mainConfig)
        else:
            return ds_content