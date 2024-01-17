Secure File Transferring

Overview

This Python code implements a secure file transfer system between a client (Alice) and a server (Bob) using various encryption modes. The encryption is facilitated by the Encrypt class in the encrypt.py module, which provides methods for generating keys and encrypting data using different encryption algorithms.

Components

Alice.py
Initiates the client-side of the secure file transfer.
Connects to the server using a TCP/IP socket.
Allows the user to choose an encryption mode (ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, AESCCM).
Reads data from 'test_file_2.txt', encrypts it, and sends it to the server.
Bob.py
Implements the server-side of the secure file transfer.
Listens for incoming connections on a specified IP address and port.
Accepts the connection from Alice, receives the encryption mode, key, and encrypted data.
Decrypts the received data based on the encryption mode and saves it to 'received_file.txt'.
Decrypts the data using the appropriate decryption algorithm.
encrypt.py
Defines the Encrypt class with methods for generating keys and encrypting data.
Supports ChaCha20Poly1305, AESGCM, AESOCB3, AESSIV, and AESCCM encryption algorithms.
Encryption Modes

ChaCha20Poly1305: Uses the ChaCha20 stream cipher combined with the Poly1305 authenticator.
AESGCM: Utilizes the AES-GCM mode for authenticated encryption.
AESOCB3: Employs the AES-OCB3 mode for authenticated encryption.
AESSIV: Applies the AES-SIV mode for deterministic authenticated encryption.
AESCCM: Uses the AES-CCM mode for authenticated encryption.
Usage

Run Bob.py on the server side.
Run Alice.py on the client side and choose an encryption mode.
The client will connect to the server, send the encryption mode, key, and encrypted data.
The server will receive, decrypt, and save the data in 'received_file.txt'.
Note

The file paths, IP address, and port numbers are hardcoded and should be adjusted as needed.
This implementation focuses on encryption and does not handle issues like error handling or robustness in a real-world scenario.
Ensure that the necessary dependencies, such as the cryptography library, are installed.
