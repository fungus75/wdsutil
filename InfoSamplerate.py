from InfoBase import InfoBase


class InfoSamplerate(InfoBase):
    def get_readable_name(self):
        return "samplerate"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the samplerate of the first file in dataset")

    def get_info(self, ds_content):
        return ds_content.get(0)["samplerate"]