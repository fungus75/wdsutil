import argparse
import sys

from DsFabric import DsFabric
from DatasetLJSpeech import DatasetLJSpeech

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # register dataset-types
    ds_fab = DsFabric()
    ds_fab.register_datatype(DatasetLJSpeech())
    content = None

    parser = argparse.ArgumentParser(description='Wave DataSet Util')
    parser.add_argument('-it', '--input_type',
                        help='Input Type, possible values: '+ds_fab.get_types_as_list())
    parser.add_argument('-if', '--input_file',
                        help='Input File, use -th for help')
    parser.add_argument('-th', '--type_help', action='store_true',
                        help='Get more information about the various input and output file types')

    args = parser.parse_args()

    if args.type_help:
        ds_fab.type_help()
        sys.exit()

    if args.input_type:
        content_type = ds_fab.get(args.input_type)
        content = content_type.import_dataset(path = args.input_file)



