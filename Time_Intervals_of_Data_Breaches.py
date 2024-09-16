#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Merged_Intervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#


def Merged_Intervals(intervals: list[list[int]]):
    mins = [0] * 1441
    out = []
    head = 1
    for interval in intervals:
        start, end = interval
        for i in range(start, end+1):
            mins[i] = 1
    # function must return a 2d arra
    while True:
        try:
            start = mins.index(1, head)
            end = mins.index(0, start)
            out.append([start, end-1])
            head = end
        except:
            break
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    row = int(input().strip())

    column = int(input().strip())

    intervals1 = []

    for _ in range(row):
        intervals1.append(list(map(int, input().rstrip().split())))

    result = Merged_Intervals(intervals1)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
