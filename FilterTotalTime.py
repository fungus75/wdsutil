import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterTotalTime(FilterBase):
    def get_readable_name(self):
        return "totaltime"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements as long as the given total time is reached or surpassed.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : time-value, e.g. 30")
        print(" -fp2 (--filter_parameter2): unit of measure: s for seconds, m for minutes, h for hours")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):
        if additional_filter_parameter is None:
            raise Exception("You must provide a unit of measure")

        if additional_filter_parameter == 's':
            fact = 1
        elif additional_filter_parameter == 'm':
            fact = 60
        elif additional_filter_parameter == 'h':
            fact = 60 * 60
        else:
            raise Exception("Not allowed unit of measure: "+additional_filter_parameter+", only s, m, and h are allowed")

        if filter_parameter is None:
            raise Exception("You must provide a desired length in "+additional_filter_parameter)

        total_time = float(filter_parameter) * fact

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = total_time > 0
            total_time -= item["duration_sec"]
            self._add_newcontent_item(item, include)
        return self.new_content
