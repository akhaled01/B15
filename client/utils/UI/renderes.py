from ..http.request_creator import ClientHttpRequest
from rich.prompt import IntPrompt, Prompt
from rich.console import Console
from rich.text import Text
from .menus import *
import socket
import json
import sys


C = Console()


def UI(client_socket: socket.socket, username: str):
    try:
        display_main_menu(client_socket, username)
    except KeyboardInterrupt:
        C.print("[bold magenta] Goodbye!")
        sys.exit(0)


def display_main_menu(cs: socket.socket, username: str):
    C.clear()
    C.print(main_menu)

    choice_main = IntPrompt.ask(prompt=Text(
        "\nPlease Enter Your Choice", style="bold blue"))
    if choice_main not in [1, 2, 3]:
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_main_menu(cs, username)

    match choice_main:
        case 1:
            display_headlines_menu(cs, username)
        case 2:
            display_sources_menu(cs, username)
        case 3:
            raise KeyboardInterrupt


def display_headlines_menu(client_socket: socket.socket, username: str):
    '''
      This function displays the headlines menu.

      Parameters
      client_socket: socket.socket
      The socket connection to the server.

      username: str
      The username of the user.
    '''
    C.clear()
    C.print(headlines_menu)

    choice_main = IntPrompt.ask(prompt=Text(
        "\nPlease Enter Your Choice", style="bold blue"))

    if choice_main not in [1, 2, 3, 4, 5]:
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_headlines_menu()

    request_data = {
        "client_name": username,
    }

    request = ClientHttpRequest(client_socket)

    match choice_main:
        case 1:
            C.clear()
            keywords = Prompt.ask(
                "Enter keywords (seperated by space)").split()
            request_data["keywords"] = keywords
            pass

        case 2:
            C.clear()
            C.print(category_menu)
            request_data["category"] = IntPrompt.ask(
                "[bold blue] Enter the desired category")
            if request_data["category"] not in [1, 2, 3, 4, 5, 6, 7]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_headlines_menu()
            pass

        case 3:
            C.clear()
            C.print(country_menu)
            request_data["country"] = Prompt.ask(
                "[bold blue] Enter the desired country code")
            if request_data["country"] not in ["AU", "NZ", "CA", "AE", "ZA", "GB", "US", "MA"]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_headlines_menu()
            pass
        case 4:
            pass
        case 5:
            UI(client_socket, username)

    response_data = request.GET(url="/headlines", host="localhost:9000",
                                data=json.dumps(request_data))

    C.print(response_data.get_body())


def display_sources_menu(cs: socket.socket, username: str):
    '''
     This function displays the sources menu.
    '''
    C.print(sources_menu)
    choice_main = IntPrompt.ask(prompt=Text(
        "\nPlease Enter Your Choice", style="bold blue"))
    while choice_main not in [1, 2, 3, 4, 5]:
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_sources_menu()
        choice_main = IntPrompt.ask(
            Text("Please Enter Your Choice", style="bold blue"))
    return choice_main
