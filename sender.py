import socket
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM


def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    client_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))

    # Send the data
    message = b'Hello, server!'
    client_socket.sendall(message)
    print('Sent: {!r}'.format(message))

    # Receive the response
    data = client_socket.recv(1024)
    print('Received: {!r}'.format(data))

    # Clean up the connection
    client_socket.close()
    print('Connection closed')


if __name__ == '__main__':
    start_client()
