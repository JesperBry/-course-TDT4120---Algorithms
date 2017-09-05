# -*- coding: utf-8 -*-

# Insertion-sort
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

print(insertionSort([18,2,6,7,8,13,1,7,9,3]))
