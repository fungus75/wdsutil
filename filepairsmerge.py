import argparse
import os
import shutil
import sys


# Press the green button in the gutter to run the script.
def copy_filepairs_to_new_folder(input_folder, prefix, output_folder):
    if not os.path.isdir(input_folder):
        sys.exit("Folder does not exist:" + input_folder)

    if not os.path.isdir(output_folder):
        sys.exit("Folder does not exist:" + output_folder)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(".txt"):
            # only .txt are interesting at the moment.
            continue

        basisfilename = filename[0:-4]
        wavfile = basisfilename + ".wav"
        if not os.path.exists(os.path.join(input_folder, wavfile)):
            print(" > Warning: wav-file missing for " + filename)
            continue

        # copy to destination
        shutil.copyfile(os.path.join(input_folder, filename),
                        os.path.join(output_folder, prefix + filename))
        shutil.copyfile(os.path.join(input_folder, wavfile),
                        os.path.join(output_folder, prefix + wavfile))


if __name__ == '__main__':
    # Command-Line Parser
    parser = argparse.ArgumentParser(description='Filepairs Merge')
    parser.add_argument('-f1', '--folder1',
                        help='Input folder 1 in filepairs-format')
    parser.add_argument('-f2', '--folder2',
                        help='Input folder2 in filepairs-format')
    parser.add_argument('-p1', '--prefix1',
                        help='Prefix 1 for files from input folder 1')
    parser.add_argument('-p2', '--prefix2',
                        help="Prefix 2 for files from input folder 2")
    parser.add_argument('-of', '--output_folder',
                        help='Output folder')

    args = parser.parse_args()

    # check input parameters
    if not args.folder1:
        sys.exit("Error: you must supply -f1")

    if not args.folder2:
        sys.exit("Error: you must supply -f2")

    if not args.prefix1:
        sys.exit("Error: you must supply -p1")

    if not args.prefix2:
        sys.exit("Error: you must supply -p2")

    if not args.output_folder:
        sys.exit("Error: you must supply -of")

    # check output folder
    if os.path.exists(args.output_folder):
        sys.exit("Error: Output folder must not exist")

    # create output folder
    os.makedirs(args.output_folder)

    copy_filepairs_to_new_folder(args.folder1, args.prefix1, args.output_folder)
    copy_filepairs_to_new_folder(args.folder2, args.prefix2, args.output_folder)
