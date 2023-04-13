from InfoBase import InfoBase


class InfoLenSecAvg(InfoBase):
    def get_readable_name(self):
        return "lensecavg"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the average duration in sec value - arithmetical average")

    def get_info(self, ds_content):
        duration_sec=0
        for i in range(0,ds_content.size()):
            duration_sec += ds_content.get(i)["duration_sec"]

        return duration_sec / ds_content.size()