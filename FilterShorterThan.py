import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterShorterThan(FilterBase):
    def get_readable_name(self):
        return "shorterthan"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements that are less seconds long than the given parameter.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : time-value in seconds, e.g. 30")
        print(" -fp2 (--filter_parameter2): not used")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):

        if filter_parameter is None:
            raise Exception("You must provide a maximum length in seconds ")

        max_time = float(filter_parameter)

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = item["duration_sec"] < max_time
            self._add_newcontent_item(item, include)
        return self.new_content
