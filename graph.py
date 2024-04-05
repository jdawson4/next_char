# Author: Jacob Dawson
#
# This file will read from the trained_dicts/ directory to find the results of
# our training. We'll then create a graph depicting what the expected next char
# is! This might just be a straight display of our matrix, or it might be more
# complex, like two columns of characters, mapping from the ones on the left to
# the ones on the right. Anyway, these graphs will get saved to graphs/

import argparse
import json
import numpy as np
from matplotlib import pyplot as plt

charsToCareAbout = "abcdefghijklmnopqrstuvwxyz"


def findNextChar(trainingOutput, thisChar):
    nextChar = "s"
    nextCharProb = 0
    for k, v in trainingOutput[thisChar].items():
        if v > nextCharProb:
            nextChar = k
            nextCharProb = v
    return nextChar, nextCharProb


def graphFromFile(filename):
    with open("trained_dicts/" + filename) as f:
        trainingOutput = json.load(f)

    # IDEA 1: display as an ndarray via matplotlib!
    probArray = np.empty([26, 26], dtype=np.float32)
    indexByChar = {charsToCareAbout[i]: i for i in range(len(charsToCareAbout))}

    for ch1 in charsToCareAbout:
        for ch2 in charsToCareAbout:
            if ch1 in trainingOutput:
                if ch2 in trainingOutput[ch1]:
                    probArray[indexByChar[ch1]][indexByChar[ch2]] = trainingOutput[ch1][
                        ch2
                    ]
    # print(probArray)
    plt.imshow(probArray, interpolation="nearest")
    plt.yticks(range(len(charsToCareAbout)), charsToCareAbout)
    plt.xticks(range(len(charsToCareAbout)), charsToCareAbout)
    # plt.show()
    plt.savefig("graphs/" + filename[:-5] + "_matrix.png")


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

    results = graphFromFile(args.filename)
