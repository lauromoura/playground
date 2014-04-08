"""Introduction to Algorithms, Third Edition

Problem 2.1-4 - Adding two integer as bit arrays"""

import sys

def add_integers(a, b):
    """Adds two integers (arrays of n bits) and returns an array of n+1 bits"""

    # Specs: position [0] is the least significant bit. Position [n-1] is the
    # most significant bit

    # Loop invariant: Array of size i+1 with the result of two i bits numbers
    # added

    # Loop invariant initialization: The output array is of size 1 with zero,
    # as no numbers have been added
    output = [False]*(len(a) + 1)

    for i, (x, y) in enumerate(zip(a, b)):
        # Loop invariant maintenance: If i bits were processed, the loop
        # invariant contains i+1 bits with the current sum. After the loop,
        # the invariant contains i+1+1 contains the sum of i+1 bits

        # Table:
        # 0 + 0 + 0        = 0
        # 1 + 0 + 0        = 1
        # 1 + 1 + 0        = 0 (c 1)
        # 1 + 1 + 1        = 1 (c 1)

        has_carry = output[i]
        output[i] = (x != y) != has_carry # Double xor
        output[i+1] = (x and y) or ((x or y) and has_carry)

    # Loop invariant termination: The output array of size i+1 has the sum of
    # two arrays of i bits

    return output

def fromBitArray(a):
    x = 0;

    for i, bit in enumerate(a):
        x += bit * 2**i

    return x

def toBitArray(x, size=10):
    bits = []
    bin_str = bin(x)[2:] # Remote the leading 0b

    for i in bin_str[::-1]:
        bits.append(bool(int(i)))

    diff = size - len(bits)
    bits += [False] * diff

    return bits

def mergeArraySize(a, b):
    max_len = max(len(a), len(b))

    a.append([False]*())

def main():
    
    one = toBitArray(1, 5)
    two = toBitArray(2, 5)
    three = toBitArray(3, 5)
    five = toBitArray(5, 5)
    eleven = toBitArray(11, 5)
    twelve = toBitArray(12, 5)
    twenty = toBitArray(20, 5)
    twentysix = toBitArray(26, 5)
    seven = toBitArray(7, 5)
    fifteen = toBitArray(15, 5)

    print fromBitArray(add_integers(one, one))
    print fromBitArray(add_integers(one, two))
    print fromBitArray(add_integers(two, two))
    print fromBitArray(add_integers(eleven, twelve))
    print fromBitArray(add_integers(twentysix, twenty))
    print fromBitArray(add_integers(seven, fifteen))


if __name__ == '__main__':
    main()