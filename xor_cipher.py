from binascii import unhexlify

# Taken from https://gist.github.com/evilpacket/5973230#file-letter_freq-json-L4
# Data identical as from Wikipedia: https://en.wikipedia.org/wiki/Letter_frequency
# Including a raw frequency for SPACE based on this: http://www.data-compression.com/english.html
# even though it's relative position is more important, but this is a very simple model.
CHAR_FREQUENCY = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.360,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074,
    ' ': 13.0,
}


def calculate_score(message):
    """
    Compure score for a string based on the letter frequency.
    Ignores non alpha characters.

    >>> calculate_score('/Foz!')
    9.809
    """
    return sum([CHAR_FREQUENCY.get(char.lower(), 0) for char in message])


def xor(bytes_str, key):
    """
    XOR each byte with the key and return the joined xorred string.

    >>> xor(b'x\x1d', 23)
    'o'
    """
    return ''.join(chr(byte ^ key) for byte in bytes_str).strip()


def decipher_single_byte_xor(hex_str):
    """
    Try to guess the key and decipher the hex_str that was
    XORed with one single byte.

    Challenge 1.3: https://cryptopals.com/sets/1/challenges/3
    """
    bytes_str = unhexlify(hex_str)
    results = []
    for key in range(256):
        message = xor(bytes_str, key)
        score = calculate_score(message)
        results.append((key, score, message))

    # Sort by the top score
    return sorted(results, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    results = decipher_single_byte_xor(hex_str)
    print("Top result")
    print("Key: {0}".format(chr(results[0][0])))
    print("Message: {0}".format(results[0][2]))

    import doctest
    doctest.testmod()
