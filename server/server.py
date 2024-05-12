from utils.logging import server_logger
from utils.handler import handle_client
from rich.traceback import install
import socket
import threading
import sys

install()

HOST = '127.0.0.1'
PORT = 9090


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

server_logger.info(f"Server started at {HOST}:{PORT}")


try:
    while True:
        client_conn, address = server_socket.accept()
        server_logger.info(f"Accepted connection from {address}")
        client_thread = threading.Thread(
            target=handle_client, args=(client_conn,))
        client_thread.start()
        client_thread.join()
        client_conn.close()
except KeyboardInterrupt:
    server_logger.info(f"Server ended")
    server_socket.close()
    server_socket.shutdown(0)
    sys.exit(0)
