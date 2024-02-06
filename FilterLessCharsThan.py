import abc
import sys

from DsContent import DsContent
from FilterBase import FilterBase


class FilterLessCharsThan(FilterBase):
    def get_readable_name(self):
        return "lesscharsthan"

    def print_filter_help(self):
        print("Filter:", self.get_readable_name())
        print(" Include elements whom text is less characters long than the given parameter.")
        print("Parameters:")
        print(" -fp  (--filter_parameter) : max characters, e.g. 230")
        print(" -fp2 (--filter_parameter2): not used")

    def perform(self, ds_content, filter_parameter=None, additional_filter_parameter=None):

        if filter_parameter is None:
            raise Exception("You must provide a maximum characters count ")

        max_char = int(filter_parameter)

        for i in range(0, ds_content.size()):
            item = ds_content.get(i)
            include = len(item["text"]) <= max_char
            self._add_newcontent_item(item, include)
        return self.new_content
