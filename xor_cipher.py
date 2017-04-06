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


def calculate_score(message):
    return sum([LETTER_FREQUENCY.get(char.lower(), 0) for char in message])


def xor(left, key):
    return ''.join(chr(byte ^ key) for byte in left)


def decipher_single_byte_xor(hex_str):
    """
    Challenge 1.3: https://cryptopals.com/sets/1/challenges/3
    """
    bytes_str = unhexlify(hex_str)
    results = []
    for key in range(256):
        message = xor(bytes_str, key)
        score = calculate_score(message)
        results.append((key, score, message))

    s = sorted(results, key=lambda x: x[1], reverse=True)
    print(s[:5])


if __name__ == '__main__':
    hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    decipher_single_byte_xor(hex_str)
