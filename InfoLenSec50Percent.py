from InfoBase import InfoBase


class InfoLenSec50Percent(InfoBase):
    def get_readable_name(self):
        return "lensec50percent"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the 50% Value based on duration in sec (also known Median)")

    def get_info(self, ds_content):
        duration_sec=[]
        for i in range(0,ds_content.size()):
            duration_sec.append(ds_content.get(i)["duration_sec"])
        duration_sec.sort()

        if ds_content.size() % 2 == 1:
            idx = ds_content.size() // 2
            return duration_sec[idx]

        idx1 = ds_content.size() // 2
        idx2 = idx1 + 1

        return (duration_sec[idx1] + duration_sec[idx2])/2
