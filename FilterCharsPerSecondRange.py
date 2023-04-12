import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterCharsPerSecondRange(FilterBase):
    def get_readable_name(self):
        return "charspersecondrange"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements whom chars_per_seconds is between the given values.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : minimum border of chars_per_seconds to include")
        print(" -fp2 (--filter_parameter2): maximum border of chars_per_seconds to include")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):

        if filter_parameter is None:
            raise Exception("You must provide a minimum chars_per_seconds border")
        if additional_filter_parameter is None:
            raise Exception("You must provide a maximum chars_per_seconds border")


        min_cps = float(filter_parameter)
        max_cps = float(additional_filter_parameter)

        if min_cps>max_cps:
            raise Exception("Minimum chars_per_seconds border must not be higher than maximum chars_per_seconds border")

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = item["chars_per_sec"] >= min_cps and item["chars_per_sec"]<= max_cps
            self._add_newcontent_item(item, include)
        return self.new_content
