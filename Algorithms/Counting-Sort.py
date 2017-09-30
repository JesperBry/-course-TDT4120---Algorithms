# -*- coding: utf-8 -*-

# Counting-Sort

# A = list/array
# K = max value in A
def countingSort(A, K):
    count = [0] * (K + 1)
    for a in A:
        count[a] += 1

    for i in range(1, K + 1):
        count[i] = count[i - 1] + count[i]

    B = [None] * len(A)
    for i in range(len(A) - 1, -1, -1):
        B[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
    return B

A = [27, 4, 15, 9, 110, 0, 13, 25, 1, 17, 802, 66, 25, 45, 97, 9]
sort = countingSort(A, max(A))
print(sort)
