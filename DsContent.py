import os.path
import random

import librosa as librosa


class DsContent:
    content = []
    mainConfig = None

    def __init__(self, mainConfig):
        self.mainConfig=mainConfig
        self.content = []

    def item_generator(self,
                relativeWaveFile=None,
                relativeWaveFileNoExtension=None,
                fullPathWaveFile=None,
                basisPathWaveFile=None,
                text=None,
                lowerText=None,
                upperText=None,
                region=None,
                age=None,
                gender=None
                ):
        # basic verification
        if relativeWaveFile is None and relativeWaveFileNoExtension is None and fullPathWaveFile is None:
            raise Exception("No variant of a filename given")
        if (relativeWaveFile is not None or relativeWaveFileNoExtension is not None) and basisPathWaveFile is None:
            raise Exception("relativeWaveFile or relativeWaveFileNoExtension requires basisPathWaveFile set")

        if text is None and lowerText is None and upperText is None:
            raise Exception("At least one text must be supplied")

        # fix paths
        if relativeWaveFile is None and fullPathWaveFile is not None:
            relativeWaveFile = os.path.basename(fullPathWaveFile)
        if relativeWaveFile is None and relativeWaveFileNoExtension is not None:
            relativeWaveFile = relativeWaveFileNoExtension + ".wav"
        if relativeWaveFileNoExtension is None:
            relativeWaveFileNoExtension = relativeWaveFile[:-4]
        if basisPathWaveFile is None:
            basisPathWaveFile = os.path.dirname(fullPathWaveFile)
        if fullPathWaveFile is None:
            fullPathWaveFile = os.path.join(basisPathWaveFile,relativeWaveFile)

        # fix text
        if text is None and lowerText is not None:
            text=lowerText
        if text is None and upperText is not None:
            text=upperText
        if lowerText is None:
            lowerText = text.lower()
        if upperText is None:
            upperText = text.upper()

        # validate gender if present
        if gender is not None:
            if gender != 'm' and gender != 'f' and gender != 'd':
                if self.mainConfig['flexible']:
                    print ("Gender "+gender+" not in allowed range")
                    gender = None
                else:
                    raise Exception("Gender "+gender+" not in allowed range")

        # validate age if present
        if age is not None:
            if age != '<20' and age != '20+' and age != '30+' and age != '40+' and age != '50+' and age != '60+':
                if self.mainConfig['flexible']:
                    print("Age " + age + " not in allowed range")
                    age = None
                else:
                    raise Exception("Age " + age + " not in allowed range")

        return {
            'relativeWaveFile': relativeWaveFile,
            'relativeWaveFileNoExtension': relativeWaveFileNoExtension,
            'fullPathWaveFile': fullPathWaveFile,
            'basisPathWaveFile': basisPathWaveFile,
            'text': text,
            'lowerText': lowerText,
            'upperText': upperText,
            'region': region,
            'age': age,
            'gender': gender
        }

    def add_item(self, item):
        self._validate_item(item)

        # get Length
        item["duration_sec"]=librosa.get_duration(path=item["fullPathWaveFile"])
        item["samplerate"] = librosa.get_samplerate(path=item["fullPathWaveFile"])
        item["chars"]=len(item["text"])
        item["chars_per_sec"]=item["chars"] / item["duration_sec"]
        self.content.append(item)

    def _validate_item(self, item):
        if      item['relativeWaveFile'] is not None and \
                item['relativeWaveFileNoExtension'] is not None and \
                item['fullPathWaveFile'] is not None and \
                item['basisPathWaveFile'] is not None and \
                item['text'] is not None and \
                item['lowerText'] is not None and \
                item['upperText'] is not None:
            return
        raise Exception("Item is not complete")

    def size(self):
        return len(self.content)

    def get(self, idx):
        if (idx<0):
            return None
        if (idx>=self.size()):
            return None
        return self.content[idx]

    def shuffle(self):
        random.shuffle(self.content)