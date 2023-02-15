import socket
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_data(key, data, mode):
    backend = default_backend()
    if mode == "ChaCha20Poly1305":
        cipher = Cipher(algorithms.ChaCha20Poly1305(key), mode=None, backend=backend)
    elif mode == "AESGCM":
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
    elif mode == "AESOCB3":
        cipher = Cipher(algorithms.AES(key), modes.OCB(nonce=b'\x00' * 15), backend=backend)
    elif mode == "AESSIV":
        cipher = Cipher(algorithms.AES(key), modes.SIV(), backend=backend)
    elif mode == "AESCCM":
        iv = os.urandom(13)
        cipher = Cipher(algorithms.AES(key), modes.CCM(iv), backend=backend)
    else:
        raise ValueError("Invalid encryption mode")
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return ciphertext


def decrypt_data(key, data, mode):
    backend = default_backend()
    if mode == "ChaCha20Poly1305":
        cipher = Cipher(algorithms.ChaCha20Poly1305(key), mode=None, backend=backend)
    elif mode == "AESGCM":
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
    elif mode == "AESOCB3":
        cipher = Cipher(algorithms.AES(key), modes.OCB(nonce=b'\x00' * 15), backend=backend)
    elif mode == "AESSIV":
        cipher = Cipher(algorithms.AES(key), modes.SIV(), backend=backend)
    elif mode == "AESCCM":
        iv = os.urandom(13)
        cipher = Cipher(algorithms.AES(key), modes.CCM(iv), backend=backend)
    else:
        raise ValueError("Invalid encryption mode")
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(data) + decryptor.finalize()
    return plaintext


def send_encrypted_data(mode):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name