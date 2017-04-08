from binascii import hexlify
import itertools


def xor(char1, char2):
    """XOR 2 characters. Return a character as well."""
    return chr(ord(char1) ^ ord(char2))


def xor_encrypt(message, key):
    r"""
    Encrypt the message using repeating key XOR.
    Challenge 1.5: https://cryptopals.com/sets/1/challenges/5

    >>> xor_encrypt("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE")
    b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    """
    encrypted_letters = []
    for letter, key_char in zip(message, itertools.cycle(key)):
        xor_char = xor(letter, key_char)
        encrypted_letters.append(xor_char)

    return hexlify(''.join(encrypted_letters).encode('utf-8'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    key = 'ICE'
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    result = xor_encrypt(message, key)
    print(result)
