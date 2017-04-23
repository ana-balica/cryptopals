from binascii import a2b_base64, hexlify
from cryptopals.c1_3.xor_cipher import decipher_single_byte_xor


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

    left_hex = hexlify(left)
    right_hex = hexlify(right)
    xor_result = int(left_hex, 16) ^ int(right_hex, 16)
    return bin(xor_result).count('1')


def guess_probable_keysizes(message, top=3):
    """
    Guess most probably keysizes by computing and comparing
    hamming distances.

    :param message: encoded message in binary
    :param top: how many top results to return
    """
    # KEYSIZE between 2 and 40 is an educated/suggested guess
    distances = []
    for keysize in range(2, 41):
        local_distances = []
        for i in [0, keysize * 2]:
            left = message[i:i + keysize]
            right = message[keysize + i:(keysize + i) * 2]
            distance = get_hamming_distance(left, right)
            local_distances.append(distance)
        distance = sum(local_distances) / len(local_distances)
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


def break_vigenere_cipher(message):
    """
    Try to break repeating key XOR (also known as Vigenere),
    by guess probably keysizes, taking blocks of bytes
    of keysize, transporing them to solve them as single
    byte XORs.

    :param message: encrypted cipher in binary
    :returns: a list of possible keys that were used
    """
    keysizes = guess_probable_keysizes(message, top=10)
    probable_keys = []
    for keysize, _ in keysizes:
        chunks = get_chunks(message, keysize)
        blocks = transpose(chunks)
        key = ''
        for block in blocks:
            block_bytes = block.encode('utf-8')
            block_hex = hexlify(block_bytes)
            result = decipher_single_byte_xor(block_hex)
            block_key = chr(result[0][0])
            key = "{0}{1}".format(key, block_key)
        probable_keys.append(key)
    return probable_keys


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    message = get_encoded_message()
    keys = break_vigenere_cipher(message)
    print(keys)
