# Author: Jacob Dawson
#
# This file will read the input file (from the training_files directory), and
# create the appropriate matrix (we'll save this as JSON because it should
# only be small).

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="nextChar trainer",
        description="Given a corpus, this file will generate a JSON of the likeliest next char!",
    )
    parser.add_argument(
        "filename",
        type=str,
        help="the corpus to train off of. use just the filename, the program expects to find the file in training_files/",
    )
    args = parser.parse_args()
    print(args.filename)
