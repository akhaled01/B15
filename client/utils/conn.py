from .http.request_creator import ClientHttpRequest
from rich.console import Console
import socket

import sys


def ServerConn(host: str, port: str, client_name: str) -> socket.socket:
    '''
      `ServerConn` establishes a connection to our Proxy server.
      It takes in the host and port of the server and the client name.
      It then sends a post request to conn client name, if `201`, return socket, else error
      and exit status 1
    '''

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # send a post request to conn client name, if 201, return socket, else error
    if ClientHttpRequest(client_socket).POST(
            "/conn", f"{host}:{port}", {"client_name": client_name}).get_status_code() == 201:
        return client_socket
    else:
        Console().print("[bold red] Error: Could not connect to server")
        sys.exit(1)
