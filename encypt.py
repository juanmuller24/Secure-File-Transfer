from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM


class Encrypt:

    # def __init__(self):
    #     self.nonce = 0
    #     self.aad = "CS645/745 Modern Cryptography"
    #
    #     f = open("test_file_1.txt", "r")
    #     data = f.read()
    #     self.data = data.encode()
    #     f.close()

    def chacha(self):
        key = ChaCha20Poly1305.generate_key()
        print(f'THE KEY ISSSSSS: {key}')
        chacha = ChaCha20Poly1305(key)
        return chacha, key

    def aesgcm(self):
        key = AESGCM.generate_key(bit_length=128)
        print(f'THE KEY ISSSSSS: {key}')
        aesgcm = AESGCM(key)
        return aesgcm, key

    def aes0cb3(self):
        key = AESOCB3.generate_key(bit_length=128)
        print(f'THE KEY ISSSSSS: {key}')
        aesocb = AESOCB3(key)
        return aesocb, key

    def aessiv(self):
        key = AESSIV.generate_key(bit_length=512)  # AES256 requires 512-bit keys for SIV
        print(f'THE KEY ISSSSSS: {key}')
        aessiv = AESSIV(key)
        return aessiv, key

    def AESCCM(self):
        key = AESCCM.generate_key(bit_length=128)
        print(f'THE KEY ISSSSSS: {key}')
        aesccm = AESCCM(key)
        return aesccm, key


