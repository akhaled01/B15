from utils.conn import ServerConn
from utils.UI.renderes import UI
from rich.prompt import Prompt
import sys

host = '127.0.0.1'
port = 9090

try:
    username = Prompt.ask("[bold green]Enter your username")
    ServerConn(username)
except KeyboardInterrupt:
    print("\nGoodbye!")
    sys.exit(0)
