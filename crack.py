#!/usr/bin/env python3
# encoding: utf-8

import sys
from itertools import combinations
from random import randint


def header():
    N = 80
    print("ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM".center(N))
    print("COPYRIGHT 2075-2077 ROBCO INDUSTRIES".center(N))
    print("-Server {n}-".format(n=randint(1, 9)).center(N))


def hamming(s1, s2):
    assert len(s1) == len(s2)
    #
    cnt = 0
    length = len(s1)
    for i in range(length):
        if s1[i] == s2[i]:
            cnt += 1
    return cnt


def classify(pairs):
    d = {}
    for w1, w2 in pairs:
        diff = hamming(w1, w2)
        if diff > 0:
            if diff not in d:
                d[diff] = []
            d[diff].append((w1, w2))
    #
    return d


def go_interactive(d):
    print()
    print("Tip: it's a good idea to start with the word that has the highest score.")
    try:
        while True:
            print()
            word = input("Guessed word: ")
            match = int(input("Number of matches: "))
            li = []
            for w1, w2 in d[match]:
                if w1 == word:
                    li.append(w2)
                if w2 == word:
                    li.append(w1)
            if len(li) == 1:
                print("The password is: ", li[0])
                return
            else:
                print("The password is one of these words: ", li)
    except (KeyboardInterrupt, EOFError):
        print()
        print("bye.")


def sep():
    print("-" * 20)


def contains(tuples, word):
    for w1, w2 in tuples:
        if w1 == word or w2 == word:
            return True
    #
    return False


def word_scores(words, d):
    result = []
    for word in words:
        cnt = 0
        for k, v in d.items():
            if contains(v, word):
                cnt += 1
        result.append((word, cnt))
    #
    result.sort(key=lambda t: t[1], reverse=True)
    for w, cnt in result:
        print("> {}  {}".format(w, cnt))


def process(fname):
    f = open(fname)
    words = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    f.close()

    pairs = list(combinations(words, 2))
    d = classify(pairs)
    header()
    print()
    word_scores(words, d)
    go_interactive(d)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} words.txt".format(sys.argv[0]))
        exit(1)
    # else
    process(sys.argv[1])
