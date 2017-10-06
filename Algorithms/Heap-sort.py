# -*- coding: utf-8 -*-

# Heap-Sort

# A = list/array
def heapSort(A):
    build_max_heap(A)

    for i in range(len(A) - 1, -1, -1):
        swap(A, 0, i)
        max_heapify(A, 0, i)

# -- START help functions --

# A = list/array
# i = largest index
# end = A.length (end of A)
def max_heapify(A, i, end):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < end and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right < end and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest, end)

def build_max_heap(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i, len(A))

# Help function for swapping values
def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

# -- END help functions --

A = [12, 13, 9, 10, 8, 0, 1, 2, 7, 4, 5, 6]
heapSort(A)
print(A)
