from binascii import unhexlify

# Taken from https://gist.github.com/evilpacket/5973230#file-letter_freq-json-L4
# Data identical as from Wikipedia: https://en.wikipedia.org/wiki/Letter_frequency
LETTER_FREQUENCY = {
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
    'z': 0.074
}


def calculate_score(string):
    return sum([LETTER_FREQUENCY[letter] for letter in string])


def xor(left, right):
    # Not sure if it works
    xor_result = bytearray(b'')
    for byte in left:
        result = byte ^ right
        xor_result.append(bytes([result]))
    return xor_result


def decipher_single_byte_xor(hex_string):
    """
    Challenge 1.3: https://cryptopals.com/sets/1/challenges/3
    """
    in_bytes = unhexlify(hex_string)
    # can update to 256 if going for extended ASCII codes
    for key in xrange(128):
        pass


# STOPPED:
# XOR all 34 bytes with 1 byte each
