from InfoBase import InfoBase


class InfoTotalSec(InfoBase):
    def get_readable_name(self):
        return "totalsec"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the total length in sec of this dataset")

    def get_info(self, ds_content):
        total_sec=0
        for i in range(0,ds_content.size()):
            total_sec += ds_content.get(i)["duration_sec"]
        return total_sec
