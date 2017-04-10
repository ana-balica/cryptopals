from binascii import a2b_base64


def get_encoded_message():
    with open('cryptopals/c1_6/6.txt', 'r') as f:
        message = f.read().strip()
        return a2b_base64(message)


def get_hamming_distance(left, right):
    """
    Calculate hamming distance - the number of different bits.

    >>> get_hamming_distance(b'this is a test', b'wokka wokka!!!')
    37

    >>> get_hamming_distance('this is a test', 'wokka wokka!!!')
    37
    """
    if isinstance(left, str):
        left = left.encode('utf-8')

    if isinstance(right, str):
        right = right.encode('utf-8')

    hd = 0
    for left_byte, right_byte in zip(left, right):
        left_bits = to_bits(left_byte)
        right_bits = to_bits(right_byte)
        hd += sum(x != y for x, y in zip(left_bits, right_bits))
    return hd


def to_bits(i):
    """Returns 8bit representation with padding if necessary."""
    return "{0:08b}".format(i)


def guess_probable_keysizes(message, top=3):
    # KEYSIZE between 2 and 40 is an educated/suggested guess
    distances = []
    for keysize in range(2, 41):
        left = message[:keysize]
        right = message[keysize:keysize * 2]
        distance = get_hamming_distance(left, right)
        distances.append((keysize, distance / keysize))
    return sorted(distances, key=lambda x: x[1])[:top]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    message = get_encoded_message()
    keysizes = guess_probable_keysizes(message)
    print(keysizes)
