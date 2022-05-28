# Copyright 2022 by Averyl Xu, Holmdel, NJ, USA.
# All rights reserved.
# This is for ACSL 2019-2020 Junior Division Programming Problem - Contest 1.
# http://www.datafiles.acsl.org/samples/contest1/C_1_JR_Transform.pdf

def transNum(n, p, d):

    list = [int(x) for x in str(n)]
    #print(list)
    if (list[len(list)-p] >= 0) and (list[len(list)-p] <= 4):
        list[len(list)-p] = (list[len(list)-p] + d) % 10
        if len(list) - p + 1 < len(list):
            list[len(list)-p+1] = 0
    elif (list[len(list)-p] >= 5) and (list[len(list)-p] <= 9):
        temp = abs(list[len(list)-p] - d)
        while (temp >= 10):
            temp = temp // 10
        list[len(list) - p] = temp
        if len(list) - p + 1 < len(list):
            list[len(list)-p+1] = 0

    s = [str(integer) for integer in list]
    a_str = "".join(s)
    new_n = int(a_str)

    #print(n)
    #print(list)
    print(new_n)

k = 5

n = [0] * k
p = [0] * k
d = [0] * k

for i in range(k):
    n[i], p[i], d[i] = map(int, input().split())

for i in range(k):
    transNum(n[i], p[i], d[i])

# Sample Inputs:
# 124987 2 3
# 540670 3 9
# 7145042 2 8
# 124987 2 523
# 4386709 1 2

# Sample Outputs:
# 124950
# 540300
# 7145020
# 124950
# 4386707
