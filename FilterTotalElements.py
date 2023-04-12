import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterTotalElements(FilterBase):
    def get_readable_name(self):
        return "totalelements"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements as long as the given total number of elements is reached.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : number of elements")
        print(" -fp2 (--filter_parameter2): not required")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):
        if filter_parameter is None:
            raise Exception("You must provide a desired number of elements")

        total_elements = int(filter_parameter)
        if total_elements > ds_content.size() and self.mainConfig['flexible']:
            total_elements = ds_content.size()

        if total_elements > ds_content.size():
            raise Exception("Number of desired elements is larger than elements exist in source dataset")

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            self._add_newcontent_item(item, i<total_elements) # add as long as index less than required number of elements
        return self.new_content
