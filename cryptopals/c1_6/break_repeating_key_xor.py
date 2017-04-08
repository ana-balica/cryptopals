def get_hamming_distance(left, right):
    """
    Calculate hamming distance - the number of different bits.

    >>> get_hamming_distance('this is a test', 'wokka wokka!!!')
    37
    """
    left_bytes = left.encode('utf-8')
    right_bytes = right.encode('utf-8')

    hd = 0
    for left_byte, right_byte in zip(left_bytes, right_bytes):
        left_bits = to_bits(left_byte)
        right_bits = to_bits(right_byte)
        hd += sum(x != y for x, y in zip(left_bits, right_bits))
    return hd


def to_bits(i):
    """Returns 8bit representation with padding if necessary."""
    return "{0:08b}".format(i)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
