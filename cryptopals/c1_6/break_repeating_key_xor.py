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


def get_chunks(block, size):
    """
    Split the iterable into chunks of size.

    :param block: any iterable
    :param size: int value bigger or equal than 1
    :returns: a generator with chunked blocks

    >>> list(get_chunks('1234567', 1))
    ['1', '2', '3', '4', '5', '6', '7']

    >>> list(get_chunks('1234567', 2))
    ['12', '34', '56', '7']
    """
    for i in range(0, len(block), size):
        yield block[i:i + size]


def transpose(chunks):
    """
    Create chunks where each chunk contains the n-th
    element of the original chunks.

    :param: iterable of bytes
    :returns: list of transposed iterables

    >>> transpose([b'123', b'456'])
    ['14', '25', '36']

    >>> transpose([b'12', b'34', b'5'])
    ['135', '24']
    """
    blocks = []
    for chunk in chunks:
        if not blocks:
            blocks = [''] * len(chunk)

        for i, byte in enumerate(chunk):
            block = blocks[i]
            block = '{0}{1}'.format(block, chr(byte))
            blocks[i] = block
    return blocks


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    message = get_encoded_message()
    keysizes = guess_probable_keysizes(message)
    print(keysizes)
