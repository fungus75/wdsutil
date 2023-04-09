from InfoBase import InfoBase


class InfoCharPerSec25Percent(InfoBase):
    def get_readable_name(self):
        return "charpersec25percent"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the 25% Value based on Characters per Sec")

    def get_info(self, ds_content):
        chars_per_sec=[]
        for i in range(0,ds_content.size()):
            chars_per_sec.append(ds_content.get(i)["chars_per_sec"])
        chars_per_sec.sort()

        idx = ds_content.size() // 4
        return chars_per_sec[idx]

