# Chapter 2, sorts and linear searches


import sys
import random
from datetime import datetime

def insertion_sort(data):
    """Sorts data in-place using insertion sort"""
    for j in range(1, len(data)):                   # n
        key = data[j] #                             # n - 1
        i = j - 1                                   # n - 1
        while i >= 0 and data[i] > key:             # sum (j=2, n) tj
            data[i+1] = data[i]                     # sum (j=2, n) tj - 1
            i -= 1                                  # sum (j=2, n) tj - 1

        data[i+1] = key                             # n - 1

    # O(n^2) swaps
    # O(n^2) comparisons
    return data

def selection_sort(data):
    """Sorts data in-place using selection sort"""

    # Loop invariant: Array from beginning to i is sorted

    # Loop invariant initialization: The first item is already sorted

    for i in range(len(data)-1):                                            # n
        # Loop invariant maintenance: The array from 0 to i-1 is already
        # sorted. After the iteration, the new item in [i] is the largest
        # item in this array, keeping it sorted

        smallest = i;                                                       # n - 1

        for j in range(i+1, len(data)):                                     # sum(j=2, n) ti
            if data[j] < data[smallest]:                                    # sum(j=2, n) ti -1
                smallest = j                                                # sum(j=2, n) ti -1

        data[i], data[smallest] = data[smallest], data[i]

    # O(n) swaps
    # O(n^2) comparisons

    return data


    # Loop invariant termination: The array is completely sorted.

def linear_search(data, key):
    
    # Loop invariant: i is the current index for the array being processed

    # Loop variant initialization: The current array is empty, so the value
    # is Nil
    i = None

    for j, x in data:
        # Loop variant maintenance: If the current value is the key, we keep
        # the invariant valid by assigning it the index of the key
        if x == key:
            i = j
            break

    # Loop variant termination: The invariant gives the index of the desired
    # key, or Nil if not found.

    return i

def main(argv=None):

    if argv is None:
        argv = sys.argv

    filename = argv[1]

    with open(filename) as handle:
        orig_data = [int(x) for x in handle.read().split()]
        size = len(orig_data)

        sorted_list = sorted(orig_data)

        for function in (insertion_sort, selection_sort):
            data = orig_data[:]
            start_time = datetime.now()
            data = function(data)
            end_time = datetime.now()

            assert(sorted_list == data)

            print "Filename: %s - Size: %s - function: %s - duration: %s" % (filename, size, function.__name__, end_time - start_time)


if __name__ == '__main__':
    main()