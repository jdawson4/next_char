# Author: Jacob Dawson
#
# This file will read the input file (from the training_files directory), and
# create the appropriate matrix (we'll save this as JSON because it should
# only be small).

import argparse
import json


def trainOnFile(filename):
    print("processing", filename)
    with open("training_files/" + filename, "r", encoding="utf8") as f:
        text = "\n".join(f.readlines())

    unicodeChars = {}
    for i in range(0, 1200):
        # print(chr(i))
        unicodeChars[chr(i)] = {}

    prevChar = False
    totalChars = 0
    for curChar in text:
        if (
            prevChar
            and (curChar.lower() in unicodeChars)
            and (prevChar.lower() in unicodeChars)
        ):
            totalChars += 1
            if curChar.lower() in unicodeChars[prevChar.lower()]:
                unicodeChars[prevChar.lower()][curChar.lower()] += 1
            else:
                unicodeChars[prevChar.lower()][curChar.lower()] = 1
        prevChar = curChar

    unicodeChars = {
        k: unicodeChars[k] for k, v in unicodeChars.items() if len(v.keys()) > 0
    }
    unicodeChars = {
        k1: {k2: v2 / totalChars for k2, v2 in v1.items()}
        for k1, v1 in unicodeChars.items()
    }
    # print(unicodeChars)

    with open("trained_dicts/" + (filename[:-4]) + ".json", "w") as f:
        json.dump(unicodeChars, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="nextChar trainer",
        description="Given a corpus, this file will generate a JSON of the likeliest next char!",
    )
    parser.add_argument(
        "filename",
        type=str,
        help="the corpus to train off of. use just the filename, the program expects to find the file in training_files/. Also accepts comma-separated filenames.",
    )
    args = parser.parse_args()

    if not args.filename:
        raise Exception("Error: arg filename not provided!")

    for file in args.filename.split(","):
        trainOnFile(file)
