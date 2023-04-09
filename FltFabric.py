import sys


class FltFabric:
    filter_dict = {}
    mainConfig = None

    def __init__(self, mainConfig):
        self.mainConfig=mainConfig

    def register_filter(self, filter=None):
        if filter is not None:
            idx = filter.get_readable_name()
            self.filter_dict[idx] = filter

    def get_filters_as_list(self):
        ret = ""
        for filter in self.filter_dict.values():
            if ret != "":
                ret += ", "
            ret += filter.get_readable_name()
        return ret

    def filter_help(self):
        for filter in self.filter_dict.values():
            filter.print_filter_help()
            print()

    def get(self, filter):
        if not filter in self.filter_dict:
            sys.exit("Error: unknown filter "+filter+", please try -fh parameter")
        return self.filter_dict[filter]
