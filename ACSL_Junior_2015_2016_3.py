# Copyright 2022 by Averyl Xu, Holmdel, NJ, USA.
# All rights reserved.
# This is for ACSL 2015-2016 Junior Division Programming Problem - Contest 3.
# http://www.datafiles.acsl.org/samples/contest3/abc_3_jr.pdf

def clearMatrix(matrix):
    #print(matrix)
    count_single = 0
    for i in range(num):
        for j in range(num):
            if len(matrix[i][j]) == 1:
                count_single += 1
                for p in range(num):
                    if (p != i):
                        matrix[p][j] = matrix[p][j].replace(matrix[i][j], "")
                for q in range(num):
                    if (q != j):
                        matrix[i][q] = matrix[i][q].replace(matrix[i][j], "")
    #print("After: ", matrix)
    return count_single

def runPuzzle(x):
    global matrix
    matrix = [["ABC"] * num for i in range(num)]
    n = int(x[0])

    for i in range(n):
        k = int(x[i * (num - 1) + 1])
        s = x[i * (num - 1) + 2].replace(" ", "")
        #print(k, s)
        matrix[(k - 1) // num][(k - 1) % num] = s
    #print(matrix)

    while (clearMatrix(matrix) < 9):
        clearMatrix(matrix)

    final_str = ""
    for i in range(num):
        for j in range(num):
            final_str += matrix[i][j]
    print(final_str)

if __name__ == "__main__":

    global num
    num = 3
    lines = 5
    biglist = []

    for i in range(lines):
        line = input().split(",")
        biglist.append(line)
    for i in range(lines):
        runPuzzle(biglist[i])

# Sample Inputs 1:
# 3, 1, A, 3, C, 8, A
# 3, 1, A, 6, C, 8, B
# 3, 1, B, 6, B, 9, C
# 2, 1, C, 5, B
# 2, 3, B, 7, A
# Expected Outputs 1:
# ABCBCACAB
# ACBBACCBA
# BCACABABC
# CABABCBCA
# CABBCAABC

# Sample Inputs 2:
# 4, 1, A, 2, B, 8, A, 9, B
# 3, 1, A, 2, B, 9, A
# 3, 3, C, 6, B, 7, C
# 2, 7, A, 6, C
# 2, 1, C, 6, A
# Expected Outputs 2:
# ABCBCACAB
# ABCCABBCA
# BACACBCBA
# CBABACACB
# CABBCAABC

