# -*- coding: utf-8 -*-

# Radix-Sort
from math import floor, log
from Counting_Sort_2 import countingSort

# A = array/list
# radix is the base of the number system
def radixSort(A, radix):
    k = max(A)
    out = A
    d = int(floor(log(k, radix) + 1))
    for i in range(d):
        out = countingSort(out, i, radix)
    return out

A = [9,3,1,4,5,7,7,2,20,55]
r = radixSort(A, max(A))
print(r)
