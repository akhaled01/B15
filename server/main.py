import socket
import threading

# Set up the server address and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)

print("Server started. Listening for incoming connections...")


def handle_client(client_socket):
    # Handle the client connection
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode()}")

        # Send a response back to the client
        client_socket.sendall(b"Hello, client!")

    # Close the client socket
    client_socket.close()


while True:
    # Accept incoming connections
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")

    # Create a new thread to handle the client connection
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket,))
    client_thread.start()
