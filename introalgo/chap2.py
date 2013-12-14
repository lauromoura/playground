
import random


def insertion_sort(data):
    """Sorts data in-place using insertion sort"""

    for i, key in enumerate(data[1:]):
        while i >= 0 and data[i] > key:
            data[i+1] = data[i]
            i -= 1

        data[i+1] = key

def main():

    for i in range(10):
        data = [int(1000*random.random()) for x in range(1000)]
        sorted_list = sorted(data)

        insertion_sort(data)

        print sorted_list == data

if __name__ == '__main__':
    main()