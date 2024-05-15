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
HOST = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((HOST, PORT))
except OSError:
    '''
      TCP sockets sometimes dont shutdown correctly.
      This causes them to continue to listen for connections
      on a closed port.
      This is a workaround to kill the process and the terminal.
    '''
    server_logger.error(
        "please kill the process and the teriminal and restart server")

server_socket.listen()  # listen for an infinite amt of clients
server_logger.info(f"listening and serving on {HOST}:{PORT}")

try:
    while True:
        client_conn, address = server_socket.accept()
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
