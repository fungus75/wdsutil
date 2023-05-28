from InfoBase import InfoBase


class InfoDumpCorpus(InfoBase):
    def get_readable_name(self):
        return "dumpcorpus"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" writes the corpus directly to screen")

    def get_info(self, ds_content):
        for i in range(0, ds_content.size()):
            print(ds_content.get(i)["text"])
        return ""
