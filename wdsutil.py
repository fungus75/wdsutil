import argparse
import sys

from DsFabric import DsFabric
from DatasetLJSpeech import DatasetLJSpeech
from IfoFabric import IfoFabric
from InfoAllSampleratesEqual import InfoAllSampleratesEqual
from InfoSamplerate import InfoSamplerate

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    mainConfig:object = {
        'flexible': False
    }

    # register dataset-types
    ds_fab = DsFabric(mainConfig)
    ds_fab.register_datatype(DatasetLJSpeech(mainConfig))

    # register info-types
    info_fab = IfoFabric(mainConfig)
    info_fab.register_info(InfoSamplerate(mainConfig))
    info_fab.register_info(InfoAllSampleratesEqual(mainConfig))
    content = None

    parser = argparse.ArgumentParser(description='Wave DataSet Util')
    parser.add_argument('-it', '--input_type',
                        help='Input Type, possible values: '+ds_fab.get_types_as_list())
    parser.add_argument('-if', '--input_file',
                        help='Input File, use -th for help')
    parser.add_argument('-th', '--type_help', action='store_true',
                        help='Get more information about the various input and output file types')
    parser.add_argument('-f', '--flexible', action='store_true',
                        help="Be flexible when something is missing")
    parser.add_argument('-i', '--info',
                        help='Get info from input dataset, use -ih for help')
    parser.add_argument('-ih', '--info_help', action='store_true',
                        help='Get more information about the various infos that could be extracted of the dataset')

    args = parser.parse_args()

    # different extended help functions
    if args.type_help:
        ds_fab.type_help()
        sys.exit()

    if args.info_help:
        info_fab.info_help()

    # some flags
    if args.flexible:
        mainConfig['flexible'] = True


    # import
    if args.input_type:
        content_type = ds_fab.get(args.input_type)
        content = content_type.import_dataset(path = args.input_file)

    # info-processing
    if args.info:
        info_type = info_fab.get(args.info)
        print(info_type.get_info(content))

