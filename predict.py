# Author: Jacob Dawson
#
# This file will read from the trained_dicts/ directory to find the results of
# our training. We'll then predict the next character based on the likeliest
# outcomes in the dictionary.

import argparse
import json

def findNextChar(trainingOutput, thisChar):
    nextChar = "s"
    nextCharProb = 0
    for k,v in trainingOutput[thisChar].items():
        if v > nextCharProb:
            nextChar = k
            nextCharProb = v
    return nextChar

def predictFromFile(filename, length, startingChar):
    with open('trained_dicts/' + filename) as f:
        trainingOutput = json.load(f)

    lastChar = startingChar
    if len(lastChar) > 1:
        lastChar = lastChar[0]
    generatedString = startingChar
    for i in range(length):
        nextChar = findNextChar(trainingOutput, lastChar)
        generatedString += nextChar
        lastChar = nextChar

    return generatedString

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
    parser.add_argument(
        "length",
        type=int,
        help="how long of a string to produce",
    )
    parser.add_argument(
        "startingChar",
        type=str,
        default='s',
        help="char to begin the string with. defaults to 's'",
    )
    args = parser.parse_args()

    if not args.filename:
        raise Exception("Error: arg filename not provided!")
    if not args.length:
        raise Exception("Error: arg length not provided!")
    if not args.startingChar:
        raise Exception("Error: arg startingChar not provided!")

    results = predictFromFile(args.filename, args.length, args.startingChar)
    print(results)
