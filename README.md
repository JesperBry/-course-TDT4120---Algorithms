# Algorithms from course TDT4120

## INSERTION-Sort

Pseudocode
```pseudocode
INSERTION-Sort(A)
  for j = 2 to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[1..j - 1].
    i = j-1
    while i > 0 and A[i] > key
      A[i+1] = A[i]
      i = i-1
    A[i+1] = key
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Insertion-sort(A).py)

## MERGE-Sort

Pseudocode
```pseudocode
MERGE-Sort(A, p, r)
  if p < r
    q = ⌊(p + r)/2⌋
    MERGE-Sort(A, p, q)
    MERGE-Sort(A, q + 1, r)
    MERGE(A, p, q, r)

MERGE(A, p, q, r)
  n1 = q - p + 1
  n2 = r - q
  let L[1..n1 + 1] and R[1..n2 + 1] be new array
  for i = 1 to n1
    L[i] = A[p + i - 1]
  for j = 1 to n2
    R[j] = A[q + j]
  L[n1 + 1] = ∞
  R[n2 + 1] = ∞
  i = 1
  j = 1
  for k = p to r
    if L[i] <= R[j]
      A[k] = L[i]
      i = i + 1
    else A[k] = R[j]
      j = j + 1
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/merge-sort.py)
