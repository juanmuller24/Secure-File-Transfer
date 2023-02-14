import socket
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM


def start_client(mode):

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    with open('test_file_1.txt', 'rb') as f:
        data = f.read(1024)
        while data:
            # Send the data
            client_socket.sendall(data)
            data = f.read(1024)

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
