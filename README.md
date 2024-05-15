# B15

![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white) ![bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white) ![nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) ![postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white) ![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

Project `B15` is a HTTP compliant TCP socket server and client. The server can accept any HTTP client (including ours of course) and acts as a proxy to [NewsAPI.org](https://newsapi.org/). The client can be used to send requests to the server and receive responses from the server. The client and server are written in Python and some tests are written in shell bash.

## Table of Content

- [B15](#b15)
  - [Table of Content](#table-of-content)
  - [Running the project](#running-the-project)
  - [About the Scripts](#about-the-scripts)
    - [The server script](#the-server-script)
    - [The client script](#the-client-script)
  - [Authors](#authors)
    - [Group B15 - Course ITNE352 - Section 2](#group-b15---course-itne352---section-2)

## Running the project

To run the project, you'll need to have Python 3.11.0 or higher installed on your machine, you'll also need to be inside a virtualenv.

To activate a virtualenv, run `python3 -m venv proj_env` and then `source proj_env/bin/activate`.

> [!IMPORTANT]  
> If you are on windows, you'll need to run `proj_env\Scripts\activate.bat` instead, or just run `activate` in powershell.

Once you have a, active virtual environment, install the project dependencies.

- `requests`
- `rich`
- `python-dotenv`

> [!TIP]
> You can install all the following by running `pip install -r requirements.txt` in the project root directory while in a virtual env.

To run the server, naviagte to the server directory and run `python server.py`.
To run the client, naviagte to the client directory and run `python client.py`.

## About the Scripts

There are mainly two scripts, but they use extensive utilities from the `utils` module in each of their directories. Read below for how its done

### The server script

- `server.py`: This is the server script that is responsible for accepting HTTP clients and multiplexing them to the required controller.
- `src/http`: This is the module that contains the `HttpRequest` and `HTTPResponseWriter` classes. It also containes the router from which we control client requests and return appropriate responses.
- `src/logging` takes care of logging the requests and responses (to JSON and to the console).
- `server/log` contains server logs and also client logs (in JSON)

> [!TIP]
> Check out the README inside `server/src/http` for more information

### The client script

- `client.py`: This is the client script that is responsible for sending HTTP requests to the server.

> [!WARNING]  
> Still under dev!

## Authors

### Group B15 - Course ITNE352 - Section 2

1. Abdulrahman Khaled Idrees - 202200729
2. Yousef Reja
