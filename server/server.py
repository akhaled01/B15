from utils.logging import server_logger
from utils.handler import handle_client
import socket
import threading
import ssl
import sys

HOST = '127.0.0.1'
PORT = 9090

server_logger.info(f"Server started at {HOST}:{PORT}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

ssl_server_socket = ssl.wrap_socket(
    server_socket, certfile='cert.pem', keyfile='key.pem', server_side=True)

try:
    while True:
        client_conn, address = ssl_server_socket.accept()
        server_logger.info(f"Accepted connection from {address}")
        client_thread = threading.Thread(
            target=handle_client, args=(client_conn,))
        client_thread.start()
except KeyboardInterrupt:
    server_logger.info(f"Server ended")
    sys.exit(0)
