from InfoBase import InfoBase


class InfoCharPerSec50Percent(InfoBase):
    def get_readable_name(self):
        return "charpersec50percent"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the 50% Value based on Characters per Sec (also known Median)")

    def get_info(self, ds_content):
        chars_per_sec=[]
        for i in range(0,ds_content.size()):
            chars_per_sec.append(ds_content.get(i)["chars_per_sec"])
        chars_per_sec.sort()

        if ds_content.size() % 2 == 1:
            idx = ds_content.size() // 2
            return chars_per_sec[idx]

        idx1 = ds_content.size() // 2
        idx2 = idx1 + 1

        return (chars_per_sec[idx1] + chars_per_sec[idx2])/2
