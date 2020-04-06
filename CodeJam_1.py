import numpy as np

t1 = int(input())  # no of test cases
for i in range(t1):
    count_r = 0
    count_c = 0
    l = []
    s = int(input())  # size of each matrix
    for i in range(s):
        r = list(map(int, input().split()))
        extra = set(r)
        if len(r) != len(extra):
            count_r += 1
        l.append(row)
    array = np.array(l)
    trace = np.trace(array)
    for j in range(s):
        c = array[ : , j]
        extra = set(tuple(c))
        if len(c) != len(extra):
            count_c += 1
    print("Case #{}: {} {} {}".format(i + 1, trace, count_r, count_c))
