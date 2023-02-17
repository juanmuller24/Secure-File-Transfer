import socket
import encypt
import time

val = 0
nonce = val.to_bytes(12, "big")
aad = b"CS645/745 Modern Cryptography"
enc = encypt.Encrypt()


def start_client(mode):
    global key, encmode, enctype

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    # sending the type of enc
    encryption_type = mode.to_bytes()
    client_socket.send(encryption_type)
    time.sleep(1)

    # to encrypt data
    if mode == 1:
        encmode, key = enc.chacha()
        # sending key
        client_socket.send(key)
        time.sleep(1)

    elif mode == 2:
        encmode, key = enc.aesgcm()
        # sending key
        client_socket.send(key)
        time.sleep(1)

    elif mode == 3:
        encmode, key = enc.aes0cb3()
        # sending key
        client_socket.send(key)
        time.sleep(1)

    elif mode == 4:
        encmode, key = enc.aessiv()
        # sending key
        client_socket.send(key)
        time.sleep(1)

    elif mode == 5:
        encmode, key = enc.AESCCM()
        # sending key
        client_socket.send(key)
        time.sleep(1)

    with open('test_file_2.txt', 'rb') as f:
        data = f.read()

        # while data:
        if mode == 1 or mode == 2 or mode == 3 or mode == 5:

            encrypted_data = encmode.encrypt(nonce, data, aad)
            bit_length = len(encrypted_data)
            bits = bit_length.to_bytes(12, 'big')
            print(f'the length of the encrypted data: {bit_length}')
            print(f'the length in bytes: {bits}')
            # sending data
            client_socket.send(bits)
            time.sleep(1)
            # sending data
            client_socket.sendall(encrypted_data)

        else:
            encrypted_data = encmode.encrypt(data, [b"CS645/745 Modern Cryptography"])
            bit_length = len(encrypted_data)
            bits = bit_length.to_bytes(12, 'big')
            print(f'the length of the encrypted data: {bit_length}')
            print(f'the length in bytes: {bits}')
            # sending data
            client_socket.send(bits)
            time.sleep(1)
            # sending data
            client_socket.sendall(encrypted_data)

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
