+++
title="sorting"
+++
# Sorting

The sorting operation arranges the numerical and alphabetical data
present in a list, in a specific order or sequence.

- [Internal Sorting](#internal-sorting)
- [External Sorting](external-sorting)

## INTERNAL SORTING

All sorting techniques which require the data set to be present in the main memory are
referred as internal sorting techniques. Examples:

- [Insertion sort](#insertion-sort)
- [Selection sort](#selection-sort)
- [Shell sort](#shell-sort)
- [Bubble sort](#bubble-sort)
- [Quick sort](#quick-sort)
- Heap sort

## EXTERNAL SORTING

External Sorting, takes place in the secondary memory of a computer. Since the number
of objects to be sorted is too large to fit in main memory. Examples:

- [Merge Sort](#merge-sort)
- Multiway Merge
- Polyphase merge

## Insertion sort

### EFFICIENCY OF INSERTION SORT

Assume that an array containing n elements is sorted using insertion sort technique.

- The minimum number of elements that must be scanned = n – 1.
- For each of the elements the maximum number of shifts possible = n – 1.
- Thus, efficiency of insertion sort = O(n2)

### ANALYSIS OF INSERTION SORT

Best case analysis : O(n)
Average case analysis : O(n2)
Worst case analysis : O(n2)

### ADVANTAGES OF INSERTION SORT

Some of the key advantages of insertion sorting technique are:

- It is one of the simplest sorting techniques that is easy to implement.
- It performs well in case of smaller lists.
- It leverages the presence of any existing sort pattern in the list, thus resulting in better efficiency.

### LIMITATIONS OF INSERTION SORT

The disadvantages associated with insertion sorting technique are as follows:

- The efficiency of O(n2) is not well suited for large sized lists.
- It is expensive because of shifting all following elements by one.

### Code

```c
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```

## Selection sort

Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

A _single iteration_ of the selection sorting technique that brings the smallest element at
the beginning of the list is called a **pass**.

### advantages

Some of the key advantages of selection sorting technique are:

- It is one of the simplest of sorting techniques.
- It is easy to understand and implement.
- It performs well in case of smaller lists.
- It does not require additional memory space to perform sorting.

### LIMITATIONS OF SELECTION SORT

The disadvantages associated with selection sort that prevent the programmers from
using it often are as follows:

- The efficiency of O(n2) is not well suited for large sized lists.
- It does not leverage the presence of any existing sort pattern in the list.

### Code

```c
// function to swap the the position of two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void selectionSort(int array[], int size) {
  for (int step = 0; step < size - 1; step++) {
    int min_idx = step;
    for (int i = step + 1; i < size; i++) {

      // To sort in descending order, change > to < in this line.
      // Select the minimum element in each loop.
      if (array[i] < array[min_idx])
        min_idx = i;
    }

    // put min at the correct position
    swap(&array[min_idx], &array[step]);
  }
}
```

## Shell sort

**Shell sort** is mainly a variation of **Insertion Sort**

Shell sort is an algorithm that first sorts the elements far apart from each other and
successively reduces the interval between the elements to be sorted. It is a generalized version
of insertion sort.
In shell sort, elements at a specific interval are sorted. The interval between the
elements is gradually decreased based on the sequence used. The performance of the shell sort
depends on the type of sequence used for a given input array.

Optimal sequences used are:

- Shell's original sequence: N/2 , N/4 , ..., 1
- Knuth's increments: 1, 4, 13, ..., (3k – 1) / 2
- Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
- Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511...
- Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
- Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....

### ANALYSIS OF SHELL SORT

Best case analysis : O(n log n)
Average case analysis : O(n1.5)
Worst case analysis : O(n2)

### ADVANTAGES OF SHELL SORT

Some of the key advantages of shell sorting technique are:

- It is one of the fastest sorting techniques for sorting small number of elements.
- It requires relatively small amount of memory.

### Code

```c
void ShellSort(int a[], int n)
{
    int gap, i, j, temp;
    for (gap = n / 2; gap > 0; gap /= 2)
    {
    for (i = gap; i < n; i += 1){
       temp = a[i];
         for (j = i; j >= gap && a[j - gap] > temp; j -= gap) {
            a[j] = a[j - gap];
            }
        a[j] = temp;
        }
    }
}
```

## Bubble Sort

Bubble sort is a sorting algorithm that compares two adjacent elements and
swaps them until they are not in the intended order.

### EFFICIENCY OF BUBBLE SORT

Assume that an array containing n elements is sorted using bubble sort technique.
Number of comparisons made in first pass = n–1.
Number of comparisons made in second pass = n – 2.
Number of comparisons made in last pass = 1.
Total number of comparisons made = (n – 1) + (n – 2) + . . . + 1
= n \* (n – 1) / 2
= O(n2)
Thus, efficiency of bubble sort = O(n2).

### ANALYSIS OF BUBBLE SORT

Best case analysis : O(n2)
Average case analysis : O(n2)
Worst case analysis : O(n2)

### ADVANTAGES OF BUBBLE SORT

Some of the key advantages of bubble sorting technique are:

- It is easy to understand and implement.
- It leverages the presence of any existing sort pattern in the list, thus resulting in
  better efficiency.

### disadvantages

The disadvantages associated with bubble sorting technique are given below:

- The efficiency of O(n2) is not well suited for large sized lists.
- It requires large number of elements to be shifted.
- It is slow in execution as large elements are moved towards the end of the list in a
  step-by-step fashion.

### Code

```c
void bubbleSort(int array[], int size) {

  for (int step = 0; step < size - 1; ++step) {
    for (int i = 0; i < size - step - 1; ++i) {
      if (array[i] > array[i + 1]) {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}
```

## Quick Sort

Quick Sort is the **most efficient **_internal sorting_** technique**.

Like Merge Sort, QuickSort is a Divide and Conquer algorithm

### ANALYSIS OF QUICK SORT

Best-case analysis : O(n log n)
Average-case analysis : O(n log n)
Worst-case analysis : O(n2)

### ADVANTAGES OF QUICK SORT

Some of the key advantages of quick sorting technique are:
- It is one of the fastest sorting algorithms.
- Its implementation does not require any additional memory.
- It has better cache performance and high speed.

### LIMITATIONS OF QUICK SORT

The disadvantages associated with quick sorting technique are as follows.
- The worst case efficiency of O(n2) is not well suited for large sized lists.
- Its algorithm is considered as a little more complex in comparison to some other
sorting techniques.

### code

```c
void QuickSort(int a[], int left, int right)
{
    int i, j, temp, pivot;
    if (left < right) {
        pivot = left;
    i = left + 1;
    j = right;
    while (i < j) {
        while (a[i] < a[pivot]) i++;
        while (a[j] > a[pivot]) j--;
        if (i < j) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }
    temp = a[pivot];
    a[pivot] = a[j];
    a[j] = temp;
    QuickSort(a, left, j - 1);
    QuickSort(a, j + 1, right);
    }
}
```

## Merge sort

Algorithm follows divide and conquer

- In dividing phase, the problem is divided into smaller problem and solved
recursively.
- In conquering phase, the partitioned array is merged together recursively.

### code

```c
void MergeSort(int arr[], int left, int right) {
  int center;
  if (left < right) {
    center = (left + right) / 2;
    MergeSort(arr, left, center);
    MergeSort(arr, center + 1, right);
    Merge(arr, left, center, right);
  }
}
void Merge(int arr[], int left, int center, int right) {
  int a[20], b[20], n1, n2, aptr, bptr, cptr, i, j;
  n1 = center - left + 1;
  n2 = right - center;
  for (i = 0; i < n1; i++)
    a[i] = arr[left + i];
  for (j = 0; j < n2; j++)
    b[j] = arr[center + 1 + j];
  aptr = 0;
  bptr = 0;
  cptr = left;
  while (aptr < n1 && bptr < n2) {
    if (a[aptr] <= b[bptr]) {
      arr[cptr] = a[aptr];
      aptr++;
    } else {
      arr[cptr] = b[bptr];
      bptr++;
    }
    cptr++;
  }
    arr[cptr] = a[aptr];
    aptr++;
    cptr++;
  }
  while (bptr < n2) {
    arr[cptr] = b[bptr];
    bptr++;
    cptr++;
  }
}
```

### ANALYSIS OF MERGE SORT

Worst case analysis : O(N log N)
Best case analysis : O(N log N)
Average case analysis : O(N log N)

### ADVANTAGES

Some of the key advantages of merge sorting technique are:
- It is a fast and stable sorting method.
- It always ensures an efficiency of O(n log n).
- It has better cache performance.
- Merge Sort is a Stable Sort.

### LIMITATIONS

The disadvantages associated with merge sorting technique are as follows
- It requires additional memory space to perform sorting. The size of the
  additional space is in direct proportion to the size of the input list.
- Even though the number of comparisons made by merge sort are nearly optimal,
  its performance is slightly lesser than that of quick sort.
- Merge sort sorts the larger amount of data making use of external storage
  device.
- It requires extra memory space.
