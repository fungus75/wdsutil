from InfoBase import InfoBase


class InfoAvgCharPerSec(InfoBase):
    def get_readable_name(self):
        return "avgcharpersec"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the average character per sec value - arithmetical average")

    def get_info(self, ds_content):
        chars_per_sec=0
        for i in range(0,ds_content.size()):
            chars_per_sec += ds_content.get(i)["chars_per_sec"]

        return chars_per_sec / ds_content.size()