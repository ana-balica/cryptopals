from binascii import b2a_base64, unhexlify


def hex_to_base64(hex_string):
    """
    Converts hex string to ASCII in base64 encoding.
    To do that, first convert hex to binary data and
    then base64 encode it. Also remove the trailing
    newline left by b2a_base64.

    Challenge 1.1: https://cryptopals.com/sets/1/challenges/1

    >>> hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    """
    return b2a_base64(unhexlify(hex_string)).rstrip()


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
