from InfoAvgCharPerSec import InfoAvgCharPerSec
from InfoBase import InfoBase
from InfoCharPerSec25Percent import InfoCharPerSec25Percent
from InfoCharPerSec50Percent import InfoCharPerSec50Percent
from InfoCharPerSec75Percent import InfoCharPerSec75Percent
from InfoCount import InfoCount
from InfoLenSec25Percent import InfoLenSec25Percent
from InfoLenSec50Percent import InfoLenSec50Percent
from InfoLenSec75Percent import InfoLenSec75Percent
from InfoLenSecAvg import InfoLenSecAvg
from InfoLenSecMax import InfoLenSecMax
from InfoLenSecMin import InfoLenSecMin
from InfoMaxCharPerSec import InfoMaxCharPerSec
from InfoMinCharPerSec import InfoMinCharPerSec
from InfoSamplerate import InfoSamplerate
from InfoTotalSec import InfoTotalSec


class InfoStats(InfoBase):
    def get_readable_name(self):
        return "stats"

    def print_info_help(self):
        print("Info:", self.get_readable_name())
        print(" directly print out various statistical numbers for the dataset")

    def get_info(self, ds_content):
        stat_class_list = [InfoCount(self.mainConfig),
                           InfoSamplerate(self.mainConfig),
                           InfoMinCharPerSec(self.mainConfig),
                           InfoCharPerSec25Percent(self.mainConfig),
                           InfoCharPerSec50Percent(self.mainConfig),
                           InfoAvgCharPerSec(self.mainConfig),
                           InfoCharPerSec75Percent(self.mainConfig),
                           InfoMaxCharPerSec(self.mainConfig),
                           InfoTotalSec(self.mainConfig),
                           InfoLenSecMin(self.mainConfig),
                           InfoLenSec25Percent(self.mainConfig),
                           InfoLenSec50Percent(self.mainConfig),
                           InfoLenSecAvg(self.mainConfig),
                           InfoLenSec75Percent(self.mainConfig),
                           InfoLenSecMax(self.mainConfig),
                           ]

        for st in stat_class_list:
            print(st.get_readable_name(), st.get_info(ds_content))

        return ""
