import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterDuplicateText(FilterBase):
    def get_readable_name(self):
        return "duplicatetext"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements with unique texts only.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : not required")
        print(" -fp2 (--filter_parameter2): not required")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):

        seen = set()

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = item["text"] not in seen
            seen.add(item["text"])
            self._add_newcontent_item(item, include)
        return self.new_content
