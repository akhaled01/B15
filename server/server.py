from utils.logging import Logger
import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 9090

logger = Logger('server.log', 'INFO')
logger.info(f"Server started at {HOST}:{PORT}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        logger.info(f"Received data: {data.decode()}")
        client_socket.sendall(b"Hello, client!")
    client_socket.close()


try:
    while True:
        client_conn, address = server_socket.accept()
        logger.info(f"Accepted connection from {address}")

        client_thread = threading.Thread(
            target=handle_client, args=(client_conn,))
        client_thread.start()
except KeyboardInterrupt:
    logger.info(f"Server ended")
    sys.exit(0)
