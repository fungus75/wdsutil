import sys


class IfoFabric:
    info_dict = {}
    mainConfig = None

    def __init__(self, mainConfig):
        self.mainConfig=mainConfig

    def register_info(self, info=None):
        if info is not None:
            idx = info.get_readable_name()
            self.info_dict[idx] = info

    def get_infos_as_list(self):
        ret = ""
        for ifo in self.info_dict.values():
            if ret != "":
                ret += ", "
            ret += ifo.get_readable_name()
        return ret

    def info_help(self):
        for ifo in self.info_dict.values():
            ifo.print_info_help()
            print()

    def get(self, info):
        if not info in self.info_dict:
            sys.exit("Error: unknown info "+info+", please try -ih parameter")
        return self.info_dict[info]
