from InfoAvgCharPerSec import InfoAvgCharPerSec
from InfoBase import InfoBase
from InfoCharPerSec25Percent import InfoCharPerSec25Percent
from InfoCharPerSec50Percent import InfoCharPerSec50Percent
from InfoCharPerSec75Percent import InfoCharPerSec75Percent
from InfoCount import InfoCount
from InfoMaxCharPerSec import InfoMaxCharPerSec
from InfoMinCharPerSec import InfoMinCharPerSec
from InfoTotalSec import InfoTotalSec


class InfoStats(InfoBase):
    def get_readable_name(self):
        return "stats"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" directly print out various statistical numbers for the dataset")

    def get_info(self, ds_content):
        stat_class_list = [InfoCount(self.mainConfig),
                           InfoMinCharPerSec(self.mainConfig),
                           InfoCharPerSec25Percent(self.mainConfig),
                           InfoCharPerSec50Percent(self.mainConfig),
                           InfoAvgCharPerSec(self.mainConfig),
                           InfoCharPerSec75Percent(self.mainConfig),
                           InfoMaxCharPerSec(self.mainConfig),
                           InfoTotalSec(self.mainConfig)
                           ]

        for st in stat_class_list:
            print(st.get_readable_name(), st.get_info(ds_content))

        return ""
