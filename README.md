# Algorithms from course TDT4120

## Insertion-sort(A)

Pseudocode
```pseudocode
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
