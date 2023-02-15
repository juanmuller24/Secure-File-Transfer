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

    key = client_socket.recv(1024)
    print(f'the key on server side ISSS: {key}')

    with open('received_file.txt', 'wb') as f:
        while True:
            # Receive the data in small chunks and retransmit it

            data = client_socket.recv(1024)

            if not data:
                break
            f.write(data)

            # message = b'Hey Juan'
            # client_socket.sendall(message)
            # print('Sent: {!r}'.format(message))

    # Clean up the connection
    with open('received_file.txt', 'rb') as file:
        data = file.read()

    chacha = ChaCha20Poly1305(key)

    print(f'data: {data}')

    ct = chacha.decrypt(nonce, data, aad)
    with open('decrypted_file.txt', 'wb') as decrypted_file:
        decrypted_file.write(ct)
    client_socket.close()
    print('Connection closed')


if __name__ == '__main__':
    start_server()
