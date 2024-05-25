from .http.request_creator import ClientHttpRequest
from rich.console import Console
from .UI.renderes import UI
import socket

import sys


def ServerConn(client_name: str):
    '''
      `ServerConn` establishes a connection to our Proxy server.
      It takes in the host and port of the server and the client name.
      It then sends a post request to conn client name, if `201`, return socket, else error
      and exit status 1
    '''

    # send a post request to conn client name, if 201, return socket, else error
    if ClientHttpRequest().POST(
            "/conn", f"localhost", 9090, {"client_name": client_name}).get_status_code() == 201:
        UI(client_name)
    else:
        Console().print("[bold red] Error: Could not connect to server")
        sys.exit(1)
