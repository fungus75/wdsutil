from InfoBase import InfoBase


class InfoLenSecMin(InfoBase):
    def get_readable_name(self):
        return "lensecmin"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the minimum duration in seconds")

    def get_info(self, ds_content):
        duration_sec=ds_content.get(0)["duration_sec"]
        for i in range(1,ds_content.size()):
            if ds_content.get(i)["duration_sec"] < duration_sec:
                duration_sec = ds_content.get(i)["duration_sec"]
        return duration_sec