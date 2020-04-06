
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:03:27 2020

@author: Ishika
"""

import numpy as np

t = int(input())  # no of test cases
for i in range(t):
    count_row = 0
    count_col = 0
    l = []
    size = int(input())  # size of each matrix
    for j in range(size):
        row = list(map(int, input().split()))
        extra = set(row)
        if len(row) != len(extra):
            count_row += 1
        l.append(row)
    arr = np.array(l)
    trace = np.trace(arr)
    for j in range(size):
        col = arr[ : , j]
        extra = set(tuple(col))
        if len(col) != len(extra):
            count_col += 1
    print("Case #{}: {} {} {}".format(i + 1, trace, count_row, count_col))
