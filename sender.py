import socket
import time

import encypt
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM

val = 0
nonce = val.to_bytes(12, "big")
aad = b"CS645/745 Modern Cryptography"
enc = encypt.Encrypt()


def start_client(mode):
    # Create a TCP/IP socket
    global key, encmode
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    # to encrypt data
    if mode == 1:
        encmode, key = enc.chacha()
        client_socket.send(key)

    elif mode == 2:
        encmode, key = enc.aesgcm()

    elif mode == 3:
        encmode, key = enc.aes0cb3()

    elif mode == 4:
        encmode, key = enc.aessiv()

    elif mode == 5:
        encmode, key = enc.AESCCM()

    with open('test_file_1.txt', 'rb') as f:
        data = f.read(1024)

        while data:
            if mode == 1 or mode == 2 or mode == 3 or mode == 5:
                time.sleep(1)
                encdata = encmode.encrypt(nonce, data, aad)
                time.sleep(1)
                client_socket.sendall(encdata)
                time.sleep(1)
                print(encdata)
                data = f.read(1024)
            else:
                encdata = encmode.encrypt(data, [b"CS645/745 Modern Cryptography"])
                client_socket.sendall(encdata)
                client_socket.send(key)
                data = f.read(1024)
            # Send the data

        # Receive the response
        # data = client_socket.recv(1024)
        # print('Received: {!r}'.format(data))

    # Clean up the connection
    client_socket.close()
    print('Connection closed')


if __name__ == '__main__':
    print('(1) ChaCha20Poly1305')
    print('(2) AESGCM')
    print('(3) AESOCB3')
    print('(4) AESSIV')
    print('(5) AESCCM')
    mode = int(input('Which Mode of encryption? (Enter Number)  '))

    start_client(mode=mode)
