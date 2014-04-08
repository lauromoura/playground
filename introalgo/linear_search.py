def add_integers(a, b):
    """Adds two integers (arrays of n bits) and returns an array of n+1 bits"""

    # Specs: position [0] is the least significant bit. Position [n-1] is the
    # most significant bit

    # Loop invariant: Array of size i+1 with the result of two i bits numbers
    # added

    # Loop invariant initialization: The output array is of size 1 with zero,
    # as no numbers have been added
    output = [0]*(len(a) + 1)

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
        output[i] = (x ^ y) || 
        output[i+1] = (x and y) or ((x or y) and has_carry)

    return output