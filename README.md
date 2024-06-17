# B15

![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white) ![bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

`B15` is a HTTP compliant TCP socket server and client. The server can accept any HTTP client (including ours of course) and acts as a proxy to [NewsAPI.org](https://newsapi.org/). The client can be used to send requests to the server and receive responses from the server. The client and server are written in Python and some tests are written in shell bash.

B15 is quite different from other TCP socket servers due to a multitude of factors, the biggest of which, is that it's compliant with the [HTTP/1.1 RFC](https://datatracker.ietf.org/doc/html/rfc2616).

> [!NOTE]
> `nginx` has inspired the idea of this project!

The hypertext transfer protocol is an application-level protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web. It is a OSI Layer 7 Protocol built on top of a OSI Layer 4 protocol (TCP).

The idea of this project, is to provide our TCP server socket the ability to accept HTTP clients from any source, and that is done by making it understand the requests, and encode responses in a very specific manner.

Going through the project, you'll find multiple modules that facilitate communication with all clients. You'll also find routing utilities that are responsible for multiplexing the requests to the required controller. You'll also find out that our client can communicate with any HTTP server *if configured of course*.

## Table of Content

- [B15](#b15)
  - [Table of Content](#table-of-content)
  - [Running B15](#running-b15)
  - [About the Scripts](#about-the-scripts)
    - [The `server` Directory](#the-server-directory)
    - [The `client` directory](#the-client-directory)
  - [Extra Concepts](#extra-concepts)
  - [`fs` Structure](#fs-structure)
  - [Authors](#authors)

## Running B15

> [!IMPORTANT]
> Use a mature Linux distro, or WSL if you are on windows!

To run B15, you'll need to have Python 3.11.0 or higher installed on your machine.

First, get an API key from [NewsAPI.org](https://newsapi.org/) and add it to a `.env` file in the root directory of the project Like this.

```env
API_KEY=<YOUR_API_KEY_HERE>
```

On each shell you open, you'll need to activate the venv, and configure it. For this, run `source config-env.sh`.

This script creates a new venv (if needed), adds all the dependencies (if needed), and configs all aliases for streamlined project execution!

To run the server, run `B15 server` from the root dir of the project.
To run the client, run `B15 client` from the root dir of the project.
To view more info (aka this README), run `B15 info` from the root dir of the project.

## About the Scripts

There are mainly two scripts, but they use extensive utilities from the `src` module in each of their directories. Read below for how its done

### The `server` Directory

- `server.py`: This is the main server script that hosts the passive server socket that accepts client connections

```python
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
HOST = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen()  # listen for an infinite amt of clients
server_logger.info(f"listening and serving on {HOST}:{PORT}")

try:
    while True:
        client_conn, address = server_socket.accept()
        client_thread = threading.Thread(
            target=HandleClient, args=(client_conn,))
        client_thread.start()
except KeyboardInterrupt:
    server_logger.info(f"Server stopped")
finally:
    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()
    sys.exit(0)

```

- `src/http`: This is the module that contains the `HttpRequest` and `HTTPResponseWriter` classes. It also containes the router from which we control client requests and return appropriate responses.

> [!TIP]
> Check out the README inside `server/src/http` for more information

- `src/logging` takes care of logging the requests and responses (to JSON and to the console).
- `server/log` contains server logs and also client logs (in `JSON`)

### The `client` directory

- `client.py` This is the main client script

```python
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
    if 'username' in locals() and username:
        # disconnect the client before ending
        if ClientHttpRequest().POST(url="/disconn", host="localhost", port=9090, data={"client_name": username}).get_status_code() == 200:
            Console().print(f"[bold white]\nGoodbye {username}!")
        else:
            Console().print(f"[bold red]\nerror disconnecting client")
    else:
        print("\nGoodbye!")
    sys.exit(0)

```

- `src/conn.py` This script establishes a new connection with the server and registers the client's name
- `src/UI` contains the scripts that are necessary to output a nice terminal UI
  - `markdowns.py` contains all the menus outputted in the terminal
  - `menus.py` contains all the menus that also make requests to the server
  - `headline_response_fmt` and `sources_response_fmt.py` format all `JSON` responses comming from the server
- `src/http` contains the `ClientHTTPRequest` module that creates and sends HTTP compliant `GET` and `POST` requests to our server. It also contains `HttpResponseParser` That parses the raw response from our server

## Extra Concepts

1. `B15` was built using test driven development, you can see all the shell scripts used to test in the `tests` directory, and use them too!
   1. To use them, run `sudo chmod 777 *` inside the `tests` directory, and then run `./<script-name>`
2. A `.env` file was used to ensure security of our API key, and is loaded inside the `server.py` script using the `dotenv` package
3. A python `.gitignore` template was used to not push any unimportant scripts
4. B15 server adapts to any HTTP client, including `Postman` or `curl`!
   1. You may also build other clients using Js, Go, or anything really 😄
5. Shell script is extensively used to run B15
6. `B15` is fully thread safe, and uses concurrency concepts like mutex locks to manage race conditions between multiple clients
7. Last but not least, a great terminal UI is used for `B15`, provided by the `rich` module

## `fs` Structure

```shell
.
├── client
│   ├── client.py
│   └── src
│       ├── conn.py
│       ├── http
│       │   ├── request_creator.py
│       │   └── response_parser.py
│       └── UI
│           ├── headline_response_fmt.py
│           ├── markdowns.py
│           ├── menus.py
│           └── sources_response_fmt.py
├── config-env.sh
├── LICENSE
├── README.md
├── requirements.txt
├── scripts
│   ├── client.sh
│   ├── run.sh
│   └── server.sh
├── server
│   ├── log
│   │   └── json
│   │       ├── B15_aa_1.1.json
│   │       ├── B15_aa_None.json
│   │       ├── B15_ab_1.1.json
│   │       ├── B15_ab_None.json
│   │       ├── B15_ak_1.1.json
│   │       ├── B15_ak_1.3.json
│   │       ├── B15_ak_2.1.json
│   │       ├── B15_ak_2.3.json
│   │       └── B15_ak_None.json
│   ├── server.py
│   └── src
│       ├── controllers
│       │   ├── headlines.py
│       │   ├── README.md
│       │   └── sources.py
│       ├── handler.py
│       ├── http
│       │   ├── request_parser.py
│       │   ├── response_writer.py
│       │   └── router.py
│       └── utils
│           ├── client_logging.py
│           ├── data_validation.py
│           └── server_logging.py
└── tests
    ├── test_concurrency.sh
    ├── test_conn.sh
    ├── test_headlines.sh
    ├── test_sources.sh
    └── test_status_codes.sh

22 directories, 40 files
```

## Authors

Group B15 - Course ITNE352 - Section 2

1. Abdulrahman Khaled Idrees - 202200729
2. Yousef Raja Salem - 202109958
