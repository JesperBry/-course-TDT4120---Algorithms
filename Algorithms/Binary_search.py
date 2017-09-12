# -*- coding: utf-8 -*-

# Binary search
# Be careful collection must be sorted, otherwise result will be unpredictable

# A = list/array
# p = first index
# r = last index
# v = search value
def bisect(A, p, r, v):
    i = p
    if p < r:
        q = (p + r)//2
        if v <= A[q]:
            i = bisect(A, p, q, v)
        else:
            i = bisect(A, q + 1, r, v)
    return i # Returns the index for the searched value (v)

A = [1, 2, 2, 3, 4, 5, 6, 7]
B = [10, 11, 12, 13, 14]
binarySearch = bisect(A, 0, len(A) - 1, 4)
print(binarySearch)
