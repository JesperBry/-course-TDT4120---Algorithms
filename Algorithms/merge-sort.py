# -*- coding: utf-8 -*-

import sys

# MERGE-Sort
def mergeSort(A, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

# merge
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0]*(n1 + 1)
    R = [0]*(n2 + 1)
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = sys.maxsize # maximum value a variable of type Py_ssize_t can take
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


A=[2,6,16,8,7,6,4,5,7,12]

print('before sort', A)
mergeSort(A, 0, len(A)-1)
print('after sort', A)
