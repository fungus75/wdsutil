import os.path

import librosa as librosa


class DsContent:
    content = []
    mainConfig = None

    def __init__(self, mainConfig):
        self.mainConfig=mainConfig

    def item_generator(self,
                relativeWaveFile=None,
                relativeWaveFileNoExtension=None,
                fullPathWaveFile=None,
                basisPathWaveFile=None,
                text=None,
                lowerText=None,
                upperText=None
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

        return {
            'relativeWaveFile': relativeWaveFile,
            'relativeWaveFileNoExtension': relativeWaveFileNoExtension,
            'fullPathWaveFile': fullPathWaveFile,
            'basisPathWaveFile': basisPathWaveFile,
            'text': text,
            'lowerText': lowerText,
            'upperText': upperText
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

