import socket


def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = (socket.gethostbyname(socket.gethostname()), 12346)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(*server_address))

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))

        # Receive the data in small chunks and retransmit it
        data = client_socket.recv(1024)
        print('Received: {!r}'.format(data))
        if data:
            message = b'Hey Juan'
            client_socket.sendall(message)
            print('Sent: {!r}'.format(message))

        # Clean up the connection
        client_socket.close()
        print('Connection closed')


if __name__ == '__main__':
    start_server()
