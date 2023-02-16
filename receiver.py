import socket

from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM

val = 0
nonce = val.to_bytes(12, "big")
aad = b"CS645/745 Modern Cryptography"


def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(*server_address))

    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(*client_address))

    mode = client_socket.recv(1024)
    encryption_type = int.from_bytes(mode, byteorder="big")
    print(f'the mode is : {encryption_type}')

    key = client_socket.recv(1024)
    print(f'the key is : {key}')

    bits = client_socket.recv(1024)
    bits_len = int.from_bytes(bits, byteorder="big")
    print(f'the length of received: {bits}')
    print(f'the length of the bit: {bits_len}')

    with open('received_file.txt', 'wb') as f:

        data = client_socket.recv(bits_len)

        if int(encryption_type) == 1:
            chacha = ChaCha20Poly1305(key)
            ct = chacha.decrypt(nonce, data, aad)
            with open('decrypted_file.txt', 'wb') as decrypted_file:
                decrypted_file.write(ct)
        elif int(encryption_type) == 2:
            aesgcm = AESGCM(key)
            ct = aesgcm.decrypt(nonce, data, aad)
            with open('decrypted_file.txt', 'wb') as decrypted_file:
                decrypted_file.write(ct)
        elif int(encryption_type) == 3:
            aes0cb3 = AESOCB3(key)
            ct = aes0cb3.decrypt(nonce, data, aad)
            with open('decrypted_file.txt', 'wb') as decrypted_file:
                decrypted_file.write(ct)
        elif int(encryption_type) == 4:
            aessiv = AESSIV(key)
            ct = aessiv.decrypt(data, aad)
            with open('decrypted_file.txt', 'wb') as decrypted_file:
                decrypted_file.write(ct)
        elif int(encryption_type) == 5:
            aesccm = AESCCM(key)
            ct = aesccm.decrypt(nonce, data, aad)
            with open('decrypted_file.txt', 'wb') as decrypted_file:
                decrypted_file.write(ct)

        f.write(data)

        # message = b'Hey Juan'
        # client_socket.sendall(message)
        # print('Sent: {!r}'.format(message))

    # Clean up the connection
    client_socket.close()
    print('Connection closed')


if __name__ == '__main__':
    start_server()
