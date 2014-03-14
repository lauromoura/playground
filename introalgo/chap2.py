
import random
import sys
import math
import time

def insertion_sort(data):
    """Sorts data in-place using insertion sort"""

    for i, key in enumerate(data[1:]):
        while i >= 0 and data[i] > key:
            data[i+1] = data[i]
            i -= 1

        data[i+1] = key

def time_sort(n):
    data = [int(1000*random.random()) for x in range(n)]
    start_time = time.time()
    insertion_sort(data)
    # data.sort()
    end_time = time.time()

    print "Size:", n, " time: ", end_time - start_time
    return end_time - start_time

def main(argv=None):

    if argv is None:
        argv = sys.argv

    sizes = []
    times = []

    for i in range(1, int(argv[1])+1):
        n = 2**i
        sizes.append(n)
        times.append(time_sort(n))

if __name__ == '__main__':
    main()