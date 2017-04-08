def xor_hex(hex1, hex2):
    """
    Compute XOR between two equal-length buffers in hex.
    Result is also a hex represented as a string.

    Challenge 1.2: https://cryptopals.com/sets/1/challenges/2

    >>> xor_hex("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    '746865206b696420646f6e277420706c6179'
    """
    xor_result = int(hex1, 16) ^ int(hex2, 16)
    return '{0:x}'.format(xor_result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
