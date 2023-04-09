from InfoBase import InfoBase


class InfoMinCharPerSec(InfoBase):
    def get_readable_name(self):
        return "mincharpersec"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the minimum character per sec value")

    def get_info(self, ds_content):
        chars_per_sec=ds_content.get(0)["chars_per_sec"]
        for i in range(1,ds_content.size()):
            if ds_content.get(i)["chars_per_sec"] < chars_per_sec:
                chars_per_sec = ds_content.get(i)["chars_per_sec"]
        return chars_per_sec