#!/usr/bin/env python
"""generator.py by michael wehrmeister, 2016-09-14
generates tavern names for D&D
"""

import random

def main():
    adjectivelist = open('adjectives.txt').read().splitlines()
    nounlist = open('nouns.txt').read().splitlines()

    tavernStyle = randomNum(0,99)
    if tavernStyle < 25:                #one noun and one adj
        nouns = randomNouns(1)
        adjs = randomAdjs(1)
    if tavernStyle >= 25 and tavernStyle < 50: #two nouns and one adjective
        nouns = randomNouns(2)
        adjs = randomAdjs(1)
    if tavernStyle >= 50 and tavernStyle < 75: #two nouns and two adjectives
        nouns = randomNouns(2)
        adjs = randomAdjs(2)
    if tavernStyle >= 75 and tavernStyle < 100: #two nouns
        nouns = randomNouns(2)
        adjs = randomAdjs(0)

    return formTavern(adjs, nouns)

def randomNum(x, y):
    return random.randint(x,y)

def randomNouns(num):
    with open('nouns.txt') as f:
        size = sum(1 for l in f)
    nouns = []
    for x in range(num):
        nouns.append(randomNum(0, size-1))
    return nouns

def randomAdjs(num):
    with open('adjectives.txt') as f:
        size = sum(1 for l in f)
    adjs = []
    for x in range(num):
        adjs.append(randomNum(0, size-1))
    return adjs

def formTavern(x, y):
    adjectivelist = open('adjectives.txt').read().splitlines()
    nounlist = open('nouns.txt').read().splitlines()
    msg = "Your Tavern name is: The "
    if len(y) == 1:
        msg = msg + adjectivelist[x[0]] + " " + nounlist[y[0]]
    elif len(y) == 2:
        if len(x) == 0:
            msg = msg + nounlist[y[0]] + " & The " + nounlist[y[1]]
        elif len(x) == 1:
            msg = msg + adjectivelist[x[0]] + " " + nounlist[y[0]] + " & The " + nounlist[y[1]]
        elif len(x) == 2:
            msg = msg + adjectivelist[x[0]] + " " + nounlist[y[0]] + " & The " + adjectivelist[x[1]] + " " + nounlist[y[1]]

    return msg



if __name__ == "__main__":
    main()

