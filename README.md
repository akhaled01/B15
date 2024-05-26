# B15

![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white) ![bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

`B15` is a HTTP compliant TCP socket server and client. The server can accept any HTTP client (including ours of course) and acts as a proxy to [NewsAPI.org](https://newsapi.org/). The client can be used to send requests to the server and receive responses from the server. The client and server are written in Python and some tests are written in shell bash.

Our project is a quite different due to a multitude of factors, the biggest of which, is that it's compliant with the [HTTP/1.1 RFC](https://datatracker.ietf.org/doc/html/rfc2616).

> [!NOTE]
> `nginx` has inspired the idea of this project!

The hypertext transfer protocol is an application-level protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web. It is a OSI Layer 7 Protocol built on top of a OSI Layer 4 protocol (TCP).

The idea of this project, is to provide our TCP server socket the ability to accept HTTP clients from any source, and that is done by making it understand the requests, and encode responses in a very specific manner.

Going through the project, you'll find multiple modules that facilitate communication with all client. You'll also find routing utilities that are responsible for multiplexing the requests to the required controller.

## Table of Content

- [B15](#b15)
  - [Table of Content](#table-of-content)
  - [Running the project](#running-the-project)
  - [About the Scripts](#about-the-scripts)
    - [The `server` Directory](#the-server-directory)
    - [The `client` directory](#the-client-directory)
  - [Extra Concepts](#extra-concepts)
  - [Authors](#authors)
          - [Group B15 - Course ITNE352 - Section 2](#group-b15---course-itne352---section-2)

## Running the project

> [!IMPORTANT]
> Use a mature Linux distro to run this project

To run the project, you'll need to have Python 3.11.0 or higher installed on your machine.

First, get an API key from [NewsAPI.org](https://newsapi.org/) and add it to a `.env` file in the root directory of the project Like this.

```env
API_KEY=<YOUR_API_KEY_HERE>
```

On each shell you open, you'll need to activate the venv, and configure it. For this, run `source config-env.sh`.

This script creates a new venv (if needed), adds all the dependencies (if needed), and configs all aliases for streamlined project execution!

To run the server, run `B15 server` from the root dir of the project.
To run the client, run `B15 client` from the root dir of the project.

## About the Scripts

There are mainly two scripts, but they use extensive utilities from the `src` module in each of their directories. Read below for how its done

### The `server` Directory

- `server.py`: This is the main server script that hosts the passive server socket that accepts client connections
- `src/http`: This is the module that contains the `HttpRequest` and `HTTPResponseWriter` classes. It also containes the router from which we control client requests and return appropriate responses.

> [!TIP]
> Check out the README inside `server/src/http` for more information

- `src/logging` takes care of logging the requests and responses (to JSON and to the console).
- `server/log` contains server logs and also client logs (in `JSON`)

### The `client` directory

- `client.py` This is the main client script
- `src/conn.py` This script establishes a new connection with the server and registers the client's name
- `src/UI` contains the scripts that are necessary to output a nice terminal UI
  - `markdowns.py` contains all the menus outputted in the terminal
  - `menus.py` contains all the menus that also make requests to the server
  - `headline_response_fmt` and `sources_response_fmt.py` format all `JSON` responses comming from the server
- `src/http` contains the `ClientHTTPRequest` module that creates and sends HTTP compliant `GET` and `POST` requests to our server. It also contains `HttpResponseParser` That parses the raw response from our server

## Extra Concepts

1. `B15` was built using test driven development, you can see all the shell scripts used to test in the `tests` directory, and use them too!
   1. To use them, run `sudo chmod 777 *` inside the `tests` directory, and then run `./<script-name>`
2. A `.env` file was used to ensure security of our API key
3. A python `.gitignore` template was used to not push any unimportant scripts
4. This project adapts to any HTTP client, including `Postman` or `curl`!
   1. You may also build other clients using Js, Go, or anything really 😄
5. Shell script is extensively used to run this project
6. `B15` is fully thread safe, and uses concurrency concepts like mutex locks to manage race conditions between multiple clients

## Authors

###### Group B15 - Course ITNE352 - Section 2

1. Abdulrahman Khaled Idrees - 202200729
2. Yousef Raja Salem - 202109958
