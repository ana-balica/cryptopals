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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
