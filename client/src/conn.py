from .http.request_creator import ClientHttpRequest
from .UI.menus import display_main_menu
from rich.console import Console
import sys


def ServerConn(client_name: str):
    '''
      `ServerConn` establishes a connection to our Proxy server.
      It takes in the host and port of the server and the client name.
      It then sends a post request to conn client name, if `201`, return socket, else error
      and exit status 1
    '''

    # send a post request to conn client name, if 201, return socket, else error
    # if the satus code is 409 (CONFLICT), the username already exists
    conn_status_code = ClientHttpRequest().POST(
        "/conn", "localhost", 9090, {"client_name": client_name}).get_status_code()

    if conn_status_code == 201:
        display_main_menu(client_name)
    else:
        if conn_status_code == 409:
            Console().print("[bold red]409 - This Username already exists")
        else:
            Console().print("[bold red]Error: Could not connect to server")
        sys.exit(1)
