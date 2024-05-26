from ..http.request_creator import ClientHttpRequest
from rich.prompt import IntPrompt, Prompt
from .headline_response_fmt import *
from .sources_response_fmt import *
from rich.console import Console
from rich.text import Text
from .markdowns import *
import json

C = Console()


def display_headlines_menu(username: str):
    '''
      This function displays the headlines menu.

      Parameters
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

    request = ClientHttpRequest()

    match choice_main:
        case 1:
            C.clear()
            keywords = Prompt.ask(
                "Enter keywords (seperated by space)").split()
            request_data["keywords"] = keywords
            request_data["option"] = 1.1
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

            match request_data["category"]:
                case 1:
                    request_data["category"] = "business"
                    pass
                case 2:
                    request_data["category"] = "entertainment"
                    pass
                case 3:
                    request_data["category"] = "general"
                    pass
                case 4:
                    request_data["category"] = "health"
                    pass
                case 5:
                    request_data["category"] = "science"
                    pass
                case 6:
                    request_data["category"] = "sports"
                    pass
                case 7:
                    request_data["category"] = "technology"
                    pass

            request_data["option"] = 1.2
            pass

        case 3:
            C.clear()
            C.print(country_menu)

            request_data["country"] = Prompt.ask(
                "[bold blue] Type the desired country code")
            if request_data["country"].lower() not in [code.lower() for code in ["AU", "NZ", "CA", "AE", "ZA", "GB", "US", "MA"]]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_headlines_menu()

            request_data["option"] = 1.3
            pass
        case 4:
            request_data["option"] = 1.4
            pass
        case 5:
            display_main_menu(username)

    response_data = request.GET(
        uri="/headlines", data=json.dumps(request_data))

    articles = json.loads(response_data.get_body())["message"]
    fmt_headline_response(articles)
    headline_choice = IntPrompt.ask(
        "[bold green]please enter the desired headline number")
    if headline_choice not in range(1, len(articles) + 1):
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_headlines_menu()
    fmt_headline_details(articles[headline_choice - 1])
    input("")
    display_main_menu(username)


def display_sources_menu(username: str):
    '''
     This function displays the sources menu.
    '''
    C.print(sources_menu)
    choice_main = IntPrompt.ask(prompt=Text(
        "\nPlease Enter Your Choice", style="bold blue"))

    if choice_main not in [1, 2, 3, 4, 5]:
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_sources_menu()

    request_data = {
        "client_name": username,
    }

    request = ClientHttpRequest()

    C.clear()
    match choice_main:
        case 1:
            C.print(category_menu)
            request_data["option"] = 2.1

            category = IntPrompt.ask(
                "[bold blue]Enter the desired category")

            if category not in [1, 2, 3, 4, 5, 6, 7]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_sources_menu()

            match category:
                case 1:
                    category = "business"
                    pass
                case 2:
                    category = "entertainment"
                    pass
                case 3:
                    category = "general"
                    pass
                case 4:
                    category = "health"
                    pass
                case 5:
                    category = "science"
                    pass
                case 6:
                    category = "sports"
                    pass
                case 7:
                    category = "technology"
                    pass

            request_data["category"] = category
        case 2:
            C.clear()
            C.print(country_menu)
            request_data["option"] = 2.2
            country = Prompt.ask(
                "[bold blue]Type the desired country code")
            if country.lower() not in [code.lower() for code in ["AU", "NZ", "CA", "AE", "ZA", "GB", "US", "MA"]]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_sources_menu()
            request_data["country"] = country

        case 3:
            C.clear()
            C.print(language_menu)
            request_data["option"] = 2.3
            language = Prompt.ask(
                "[bold blue]Type the desired language code")
            if language.lower() not in [code.lower() for code in ["en", "ar"]]:
                C.print(Text("Invalid Choice", style="bold red"))
                input("")
                display_sources_menu()

            request_data["language"] = language

        case 4:
            request_data["option"] = 2.4
            pass

        case 5:
            display_main_menu(username)

    response_data = request.GET(
        uri="/sources", data=json.dumps(request_data))

    sources = json.loads(response_data.get_body())["message"]
    fmt_sources_list(sources)
    source_choice = IntPrompt.ask(
        "[bold green]please enter the desired source number")
    if source_choice not in range(1, len(sources) + 1):
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_sources_menu()
    fmt_source_details(sources[source_choice - 1])
    input("")
    display_main_menu(username)


def display_main_menu(username: str):
    C.clear()
    C.print(main_menu)

    choice_main = IntPrompt.ask(prompt=Text(
        "\nPlease Enter Your Choice", style="bold blue"))
    if choice_main not in [1, 2, 3]:
        C.print(Text("Invalid Choice", style="bold red"))
        input("")
        display_main_menu(username)

    match choice_main:
        case 1:
            display_headlines_menu(username)
        case 2:
            display_sources_menu(username)
        case 3:
            raise KeyboardInterrupt
