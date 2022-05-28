# Copyright 2022 by Averyl Xu, Holmdel, NJ, USA.
# All rights reserved.
# This is for ACSL 2017-2018 Junior Division Programming Problem - Contest 4.
# http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_jr.pdf

import bisect
import re

def getNumElement(str, n):
    s = []
    mylist = []
    myhash = []

    res = re.sub(r'[^a-zA-Z]', '', str)
    for i in range(len(res)):
        bisect.insort_left(s, res[i].upper())
        #print(s)
        if (len(s) >= n):
            mylist += s[n-1]

    myhash = set(mylist)
    #print(mylist)
    #print(myhash)
    return(len(myhash))

if __name__ == "__main__":
    k = 5
    n_list = []
    str_list = []

    for i in range(k):
        n, str = input().split(maxsplit=1)
        n_list.append(int(n))
        str_list.append(str)

    for i in range(k):
        #print(n_list[i], str_list[i])
        print(getNumElement(str_list[i], n_list[i]))

# Sample Inputs:
# 2 Computer
# 2 COMPUTER bat
# 3 COMPUTER
# 4 ACSL is fun
# 9 the xylophone
# Expected Outputs:
# 3
# 5
# 2
# 3
# 4