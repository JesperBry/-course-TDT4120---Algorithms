# -*- coding: utf-8 -*-

# Bucket-Sort

# A = list/array
def bucketSort(A):
    n = max(A)
    counts = [0]*(1+n)
    for i in A:
        counts[i] += 1
    sorted_A = []
    for j in range(0, len(counts)):
        sorted_A.extend([j]*counts[j])
    A[:] = sorted_A
    return sorted_A


A = [18,2,6,7,8,13,1,7,9,3]
bucketSort(A)
print(A)
