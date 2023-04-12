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
        for i in range(0,ds_content.size()):
            self._add_content_item(ds_content.get(i), True) #default: add anything
        return self.new_content