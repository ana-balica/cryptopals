from cryptopals.c1_3.xor_cipher import decipher_single_byte_xor


def get_encoded_messages():
    """
    Returns a generator of strings read from file.
    """
    with open('cryptopals/c1_4/4.txt', 'r') as f:
        for line in f:
            yield line.strip()


def find_encrypted_message(encoded_messages):
    """
    Find and decrypt the message that was encrypted
    by a single char XOR. Returns all the results
    sorted by a letter frequency score.

    Challenge 1.4: https://cryptopals.com/sets/1/challenges/4
    """
    top_results = []
    for hex_str in encoded_messages:
        hex_str = hex_str
        results = decipher_single_byte_xor(hex_str)
        top_results.append(results[0])

    return sorted(top_results, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    messages = get_encoded_messages()
    results = find_encrypted_message(messages)
    print("Top result")
    print("Key: {0}".format(chr(results[0][0])))
    print("Message: {0}".format(results[0][2]))

