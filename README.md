# Algorithms from course TDT4120

| Algorithm             | WC             | AC/E      |
| --------------------- |:--------------:| ---------:|
| <project URL#<INSERTION-Sort>        | Θ(n^2)         | Θ(n^2)    |
| MERGE-Sort            | Θ(nlgn)        | Θ(nlgn)   |
| Binary search         | Θ(lgn)         | Θ(lgn)    |
| Quicksort             | Θ(n^2)         | Θ(nlgn)*  |
| Randomized-Quicksort  | O(nlgn)        | O(nlgn)   |
| Counting-Sort         | Θ(n+k)         | Θ(n+k)    |
| Radix-Sort            | Θ(d(n+k))      | Θ(d(n+k)) |
| Bucket-Sort           | Θ(n^2)         | Θ(n)**    |
| Heap-Sort             | O(nlgn)        | O(nlgn)   |

*Expected, Randomized-Quicksort

**Average-case

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

## Binary search

Pseudocode
```pseudocode
Bisect(A, p, r, v)
  i = p
  if p < r
    q = ⌊(p + r)/2⌋
    if v <= A[q]
      i = Bisect(A, p, q, v)
    else i = Bisect(A, q + 1, r, v)
  return i  
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Binary_search.py)

## Quicksort

Pseudocode
```pseudocode
Partition(A, p, r)
  x = A[r]
  i = p - 1
  for j = p to r - 1
    if A[j] <= x
      i = i + 1
      exchange A[i] with A[j]
  exchange A[i + 1] with A[r]
  return i + 1

Quicksort(A, p, r)
  if p < r
    q = Partition(A, p, r)
    Quicksort(A, p, q - 1)
    Quicksort(A, q + 1, r)
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Quicksort.py)

## Randomized-Quicksort

Pseudocode
```pseudocode
Randomized-Partition(A, p, r)
  i = Random(p, r)
  exchange A[r] and A[i]
  return Partition(A, p, r)

Randomized-Quicksort(A, p, r)
  if p < r
    q = Randomized-Partition(A, p, r)
    Randomized-Quicksort(A, p, q - 1)
    Randomized-Quicksort(A, q + 1, r)
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Randomized-Quicksort.py)

## Counting-Sort

Pseudocode
```pseudocode
Counting-sort(A, B, k)
  let C[0..k] be a new array
  for i = 0 to k
    C[i] = 0
  for j = 1 to A.length
    C[A[j]] = C[A[j]]+1
  for i = 1 to k
    C[i] = C[i] + C[i-1]
  for j = A.length downto 1
    B[C[A[j]]] = A[j]
    C[A[j]] = C[A[j]] - 1
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Counting-Sort.py)

## Radix-Sort

Pseudocode
```pseudocode
Radix-Sort(A,d)
  for i = 1 to d
    sort* A by digit d


*Must be stable**
**Do not exchange equal values
Use: Counting-sort, Bucket-sort or Merge-sort
```
[Python code]()

## Bucket-Sort

Pseudocode
```pseudocode
Bucket-Sort(A)
  n = A.length
  create B[0 ..n - 1]
  for i = 1 to n
    make B[i] an empty list
  for i = 1 to n
    add A[i] to B[⌊nA[i]⌋]
  for i = 0 to n - 1
    sort list B[i]
  concatenate B[0] ... B[n - 1]
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Bucket-Sort.py)

## Heap-Sort

Pseudocode
```pseudocode
Heapsort(A)
  Build-Max-Heap(A)
  for i = A.length downto 2
    exchange A[1] with A[i]
    A.size = A.size - 1
    Max-Heapify(A, 1)

Build-Max-Heap(A)
  A.size = A.length
  for i =  ⌊A.length/2⌋ downto 1
    Max-Heapify(A, i)

Max-Heapify(A, i)
  l = Left(i)        // Left(i) = 2i
  r = Right(i)       // Right(i) = 2i + 1
  if l <= A.size and A[l] > A[i]
    m = l
  else m = i
  if r <= A.size and A[r] > A[m]
    m = r
  if m != i
    exchange A[i] with A[m]
    Max-Heapify(A, m)
```
[Python code](https://github.com/JesperBry/-course-TDT4120---Algorithms/blob/master/Algorithms/Heap-sort.py)

## License

 All [python](https://github.com/JesperBry/-course-TDT4120---Algorithms/tree/master/Algorithms) algorithms are licensed under the [MIT](http://opensource.org/licenses/MIT) license.
