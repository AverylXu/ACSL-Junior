# Copyright 2022 by Averyl Xu, Holmdel, NJ, USA.
# All rights reserved.
# This is for ACSL 2018-2019 Junior Division Programming Problem - Contest 2.
# http://www.datafiles.acsl.org/samples/contest2/c2-jr-prog.pdf

import re
from collections import Counter

def countDis(str):

    #1. The number of different letters.
    #   This will be a number from 1 to 26, inclusive.
    res = re.sub(r'[^a-zA-Z]', '', str)
    s = set(res.lower())
    print(len(s))

    #2. The number of vowels.
    #   Vowels are the letters a, e, i, o, and u.
    vowels = set('aeiou')
    counter1 = 0
    for c in res.lower():
        if c in vowels:
            counter1 += 1
    print(counter1)

    #3. The number of uppercase letters.
    cap = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    counter2 = 0
    for c in res:
        if c in cap:
            counter2 += 1
    print(counter2)

    #4. The number of times that the most frequent letter appears.
    #   There is no distinction between lowercase and uppercase letters.
    count = Counter(res.lower())
    k = max(count, key = count.get)
    print(res.lower().count(k))

    #5. The longest word in the sentence.
    #   If there is a tie, print the one that appears first when sorting these words alphabetically without regard to lowercase and uppercase.
    res2 = re.sub(r'[^a-zA-Z ]', '', str)
    longest = max(res2.split(), key=len)
    print(longest)

if __name__ == "__main__":

    S = input()
    #S = "The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog."
    countDis(S)