import abc

from DsContent import DsContent
from FilterBase import FilterBase


class FilterAll(FilterBase):
    def get_readable_name(self):
        return "all"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" filter all, means copy complete dataset to destination, including all.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : not required")
        print(" -fp2 (--filter_parameter2): not required")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):
        for i in range(0, ds_content.size()):
            self._add_content_item(ds_content.get(i), True)  # default: add anything
        return self.new_content
