# Author: Jacob Dawson
#
# This file will read from the trained_dicts/ directory to find the results of
# our training. We'll then create a graph depicting what the expected next char
# is! This might just be a straight display of our matrix, or it might be more
# complex, like two columns of characters, mapping from the ones on the left to
# the ones on the right.

import argparse
import json


def findNextChar(trainingOutput, thisChar):
    nextChar = "s"
    nextCharProb = 0
    for k, v in trainingOutput[thisChar].items():
        if v > nextCharProb:
            nextChar = k
            nextCharProb = v
    return nextChar


def graphFromFile(filename):
    with open("trained_dicts/" + filename) as f:
        trainingOutput = json.load(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="nextChar predictor",
        description="Given a JSON from our training file, we'll create a string of text based",
    )
    parser.add_argument(
        "filename",
        type=str,
        help="the results of our training, a JSON file that indicates how likely a character is to follow from another.",
    )
    args = parser.parse_args()

    if not args.filename:
        raise Exception("Error: arg filename not provided!")

    results = graphFromFile(args.filename, args.length, args.startingChar)
