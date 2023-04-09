from InfoBase import InfoBase


class InfoCount(InfoBase):
    def get_readable_name(self):
        return "count"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" returns the number of files in this dataset")

    def get_info(self, ds_content):
        return ds_content.size()
