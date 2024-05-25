from src.utils.server_logging import server_logger
from src.handler import HandleClient
from rich.traceback import install
from dotenv import load_dotenv
import threading
import socket
import sys

load_dotenv()  # load the .env file for API key
install()  # pretty print errors

# Expose ip interface if given as CLI argument, else localhost
HOST = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()  # listen for an infinite amt of clients
server_logger.info(f"listening and serving on {HOST}:{PORT}")

try:
    while True:
        client_conn, address = server_socket.accept()
        client_thread = threading.Thread(
            target=HandleClient, args=(client_conn,))
        client_thread.start()
except KeyboardInterrupt:
    server_logger.info(f"Server stopped")
finally:
    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()
    sys.exit(0)
