from InfoBase import InfoBase


class InfoLenSec75Percent(InfoBase):
    def get_readable_name(self):
        return "lensec75percent"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the 75% Value based on duration in Sec")

    def get_info(self, ds_content):
        duration_sec=[]
        for i in range(0,ds_content.size()):
            duration_sec.append(ds_content.get(i)["duration_sec"])
        duration_sec.sort()

        idx = (ds_content.size() * 3) // 4
        return duration_sec[idx]

