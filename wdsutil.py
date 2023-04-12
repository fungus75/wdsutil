import argparse
import sys

from DsFabric import DsFabric
from DatasetLJSpeech import DatasetLJSpeech
from FilterAll import FilterAll
from FilterTotalElements import FilterTotalElements
from FilterTotalTime import FilterTotalTime
from FltFabric import FltFabric
from IfoFabric import IfoFabric
from InfoAllSampleratesEqual import InfoAllSampleratesEqual
from InfoAvgCharPerSec import InfoAvgCharPerSec
from InfoCharPerSec25Percent import InfoCharPerSec25Percent
from InfoCharPerSec50Percent import InfoCharPerSec50Percent
from InfoCharPerSec75Percent import InfoCharPerSec75Percent
from InfoCount import InfoCount
from InfoMaxCharPerSec import InfoMaxCharPerSec
from InfoMinCharPerSec import InfoMinCharPerSec
from InfoSamplerate import InfoSamplerate
from InfoStats import InfoStats
from InfoTotalSec import InfoTotalSec

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
    info_fab.register_info(InfoMinCharPerSec(mainConfig))
    info_fab.register_info(InfoMaxCharPerSec(mainConfig))
    info_fab.register_info(InfoAvgCharPerSec(mainConfig))
    info_fab.register_info(InfoCount(mainConfig))
    info_fab.register_info(InfoTotalSec(mainConfig))
    info_fab.register_info(InfoCharPerSec25Percent(mainConfig))
    info_fab.register_info(InfoCharPerSec50Percent(mainConfig))
    info_fab.register_info(InfoCharPerSec75Percent(mainConfig))
    info_fab.register_info(InfoStats(mainConfig))

    # register filters
    filter_fab = FltFabric(mainConfig)
    filter_fab.register_filter(FilterAll(mainConfig))
    filter_fab.register_filter(FilterTotalTime(mainConfig))
    filter_fab.register_filter(FilterTotalElements(mainConfig))

    content = None

    parser = argparse.ArgumentParser(description='Wave DataSet Util')
    parser.add_argument('-it', '--input_type',
                        help='Input Type, possible values: '+ds_fab.get_types_as_list())
    parser.add_argument('-if', '--input_file',
                        help='Input File, use -th for help')
    parser.add_argument('-th', '--type_help', action='store_true',
                        help='Get more information about the various input and output file types')
    parser.add_argument('-s', '--strict', action='store_true',
                        help="Be strict when something is missing")
    parser.add_argument('-i', '--info',
                        help='Get info from input dataset, use -ih for help; possible values: '+info_fab.get_infos_as_list())
    parser.add_argument('-ih', '--info_help', action='store_true',
                        help='Get more information about the various infos that could be extracted of the dataset')
    parser.add_argument('-f', '--filter',
                        help='Copy dataset from input to output using the given filter; -fh for help; possible values: '+
                             filter_fab.get_filters_as_list())
    parser.add_argument('-fh', '--filter_help', action='store_true',
                        help='Get more information about the various filters that could be used by copying the dataset')
    parser.add_argument('-fp', '--filter_parameter',
                        help='Optional parameter required for some filters, use -fh for help')
    parser.add_argument('-fp2', '--filter_parameter2',
                        help='Another optional parameter required for some filters, use -fh for help')
    parser.add_argument('-ot', '--output_type',
                        help='Input Type, possible values: '+ds_fab.get_types_as_list())
    parser.add_argument('-of', '--output_file',
                        help='Input File, use -th for help')
    parser.add_argument('-n', '--not_filter_flag', action='store_true',
                        help='Not when processing filter: filter out the exact opposite of the normal filter behaviour')
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help='Overwrite if export-path already exist')
    parser.add_argument('-r', '--random', action='store_true',
                        help='Randomize (shuffle) the order of elements prior to export or filtering')


    args = parser.parse_args()

    # different extended help functions
    if args.type_help:
        ds_fab.type_help()
        sys.exit()

    if args.info_help:
        info_fab.info_help()
        sys.exit()

    if args.filter_help:
        filter_fab.filter_help()
        sys.exit()


    # some flags
    mainConfig['flexible'] = not args.strict
    mainConfig['not_filter_flag'] = args.not_filter_flag
    mainConfig['overwrite'] = args.overwrite

    # check exclusive-or-flags
    if args.filter and args.info:
        sys.exit("Error: Please supply -i or -f, not both!")

    # import
    if args.input_type:
        content_type = ds_fab.get(args.input_type)
        content = content_type.import_dataset(path=args.input_file)

    # info-processing
    if args.info:
        info_type = info_fab.get(args.info)
        print(info_type.get_info(content))

    # randomizing (must be done prior to filtering
    if args.random:
        content.shuffle()

    # filter-processing
    if args.filter:
        if not args.output_type:
            sys.exit("Error: you must supply -ot when using -f")
        output_type = ds_fab.get(args.output_type)
        filter_type = filter_fab.get(args.filter)
        filter_content = filter_type.perform(content, args.filter_parameter, args.filter_parameter2)
        output_type.setContent(filter_content)
        output_type.export_dataset(args.output_file)
