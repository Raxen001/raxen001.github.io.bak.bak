+++
title="searching"
+++
# Unit 5

## Linear Search

- Sequential search for the element in the list
- efficiency _o[n]_

### Advantages

- simple
- Doesn't require sorted list

### Disadvantages

- inefficient with large list
- Doesn't leverage previously sorted list

## Binary Search

### PRE REQUIREMENTS

- Need **SORTED LIST**
- best efficiency o(1)
- worst O(log2n)

### PROCEDURE

begins
by comparing the element that is present at the middle of the list. If there is a match, then the
search ends immediately and the location of the middle element is returned. However, if there
is a mismatch then it focuses the search either in the left or the right sub list depending on
whether the target element is lesser than or greater than middle element. The same
methodology is repeatedly followed until the target element is found.

### Advantages

Some of the key advantages of binary search technique are:

• It requires lesser number of iterations.
• It is a lot faster than linear search.

###disadvantages

associated with it are as follows:
• Unlike linear search, it requires the list to be sorted before search can be performed.
• In comparison to linear search, the binary search technique may seem to be a little
difficult to implement.

### Function

```c
int BinarySearch(int a[], int n, int key)
{
    int first, last, mid;
    first = 0;
    last = n - 1;
    while (first <= last)
    {
        mid = (first + last) / 2;
        if (a[mid] == key)
        return mid;
    else if (a[mid] < key)
        first = mid + 1;
    else
        last = mid - 1;
    }
    return -1;
}
```
