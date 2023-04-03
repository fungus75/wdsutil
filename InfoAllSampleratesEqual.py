from InfoBase import InfoBase


class InfoAllSampleratesEqual(InfoBase):
    def get_readable_name(self):
        return "allsampleratesequal"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns True if all samplerates are equal or False instead")

    def get_info(self, ds_content):
        samplerate=ds_content.get(0)["samplerate"]
        for i in range(1,ds_content.size()):
            if ds_content.get(i)["samplerate"] != samplerate:
                return False
        return True