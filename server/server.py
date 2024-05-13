from utils.server_logging import server_logger
from utils.kill import Kill9090
from dotenv import load_dotenv
from utils.handler import HandleClient
from rich.traceback import install
import socket
import threading
import sys

load_dotenv() # load the .env file 
install()

HOST = '127.0.0.1'
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  server_socket.bind((HOST, PORT))
except OSError:
  Kill9090()

server_socket.listen()

server_logger.info(f"Server started at {HOST}:{PORT}")

try:
    while True:
        client_conn, address = server_socket.accept()
        server_logger.info(f"Accepted connection from {address}")
        client_thread = threading.Thread(
            target=HandleClient, args=(client_conn, server_socket))
        client_thread.start()
        client_thread.join()
        client_conn.close()
except KeyboardInterrupt:
    server_logger.info(f"Server stopped")
    server_socket.shutdown(2)
    server_socket.close()
    sys.exit(0)
