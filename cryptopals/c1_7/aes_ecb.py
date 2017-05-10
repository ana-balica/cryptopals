import base64
from binascii import a2b_base64
from Crypto.Cipher import AES


def get_encoded_message(path):
    with open(path, 'r') as f:
        message = f.read()
        return base64.b64decode(message)


class AESCipher:
    def __init__(self, key, block_size=16):
        self.key = key
        self.block_size = block_size

    def decrypt(self, data, *args, **kwargs):
        cipher = AES.new(self.key, *args, **kwargs)
        decrypted_data = cipher.decrypt(data)
        return decrypted_data.decode('utf-8')

    def _pad(self, data):
        extra = self.block_size - len(data) % self.block_size
        pad = bytes(extra * chr(extra), 'utf-8')
        return data + pad

    def _unpad(self, data):
        return data[:-ord(data[len(data)-1:])]


if __name__ == '__main__':
    key = "YELLOW SUBMARINE"
    data = get_encoded_message('cryptopals/c1_7/7.txt')
    aes_cipher = AESCipher(key)
    message = aes_cipher.decrypt(data, mode=AES.MODE_ECB)
    print(message)
