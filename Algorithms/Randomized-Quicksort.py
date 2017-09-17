# -*- coding: utf-8 -*-

# Randomized-Quicksort
from random import randint

# A = list/array
# p = first index
# r = last index

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def randomized_Partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_Quicksort(A, p, r):
    if p < r:
        q = randomized_Partition(A, p, r)
        randomized_Quicksort(A, p, q - 1)
        randomized_Quicksort(A, q + 1, r)

A = [4,5,7,4,3,6,0,4,22,45,82]
print('Before: ', A)
randomized_Quicksort(A, 0, len(A) - 1)
print('After: ', A)
