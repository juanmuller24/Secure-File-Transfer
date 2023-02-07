import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
clientsocket.connect((host, port))

# send a thank you message to the client.
msg = clientsocket.recv(1024)
print(msg.decode('ascii'))

clientsocket.close()