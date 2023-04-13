import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterDurationSecRange(FilterBase):
    def get_readable_name(self):
        return "durationsecrange"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements whom duration in seconds is between the given values.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : minimum border of duration to include")
        print(" -fp2 (--filter_parameter2): maximum border of duration to include")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):

        if filter_parameter is None:
            raise Exception("You must provide a minimum duration border")
        if additional_filter_parameter is None:
            raise Exception("You must provide a maximum duration border")

        min_dur = float(filter_parameter)
        max_dur = float(additional_filter_parameter)

        if min_dur > max_dur:
            raise Exception("Minimum duration border must not be higher than maximum duration border")

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = min_dur <= item["duration_sec"] <= max_dur
            self._add_newcontent_item(item, include)
        return self.new_content
