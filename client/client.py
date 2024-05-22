from utils.conn import ServerConn
from rich.prompt import Prompt
from utils.UI.renderes import UI
import sys


def main():
    host = '127.0.0.1'
    port = 9090
    try:
        username = Prompt.ask("[bold green]Enter your username")
        client_socket = ServerConn(host, port, username)

        UI(client_socket, username=username)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
