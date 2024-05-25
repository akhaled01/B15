from src.conn import ServerConn
from rich.prompt import Prompt
import sys

try:
    username = Prompt.ask("[bold green]Enter your username")
    ServerConn(username)
except KeyboardInterrupt:
    print("\nGoodbye!")
    sys.exit(0)
