from src.http.request_creator import ClientHttpRequest
from rich.console import Console
from src.conn import ServerConn
from rich.prompt import Prompt
import sys

try:
    username = Prompt.ask("[bold green]Enter your username")
    ServerConn(username)

except ConnectionRefusedError:
    Console().print("[bold red]The Server is not live")
    sys.exit(1)

except KeyboardInterrupt:
    if username and 'username' in locals():
        # disconnect the client before ending
        if ClientHttpRequest().POST(url="/disconn", host="localhost", port=9090, data={"client_name": username}).get_status_code() == 200:
            Console().print(f"[bold white]\nGoodbye {username}!")
        else:
            Console().print(f"[bold red]\nerror disconnecting client")
    else:
        print("\nGoodbye!")
    sys.exit(0)
