from .server_logging import server_logger
from src.http.response_writer import HTTPResponseWriter
from src.http.request_parser import HttpRequest
from datetime import datetime
import json


def LogClientRequest(request: HttpRequest, response_data: dict, response_writer: HTTPResponseWriter):
    '''
      `LogClientRequest` is a function that logs the client request and the response.
      It takes in the `HttpRequest` object, the response data and the `HTTPResponseWriter` object.
      It then logs the request and response to a json file.

      Parameters:
      request (HttpRequest): The request object.
      response_data (dict): The response data.
      response_writer (HTTPResponseWriter): The response writer object.

      Returns:
      None
    '''
    with open(f"log/json/B15_{json.loads(request.get_data()).get('client_name')}_{json.loads(request.get_data()).get('option')}.json", "w") as f:
        f.write(json.dumps({
            "client_name": json.loads(request.get_data()).get("client_name"),
            "option": json.loads(request.get_data()).get("option"),
            "request": request.get_data(),
            "response": response_data,
            "response_status": str(response_writer.status_code) + " " + response_writer._get_status_message(response_writer.status_code),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }))


def LogClientConn(request: HttpRequest):
    '''
      `LogClientConn` is a function that logs the client connection.
      It takes in the `HttpRequest` object and the client socket.
      It then logs the request and response to the terminal.

      Parameters:
      request (HttpRequest): The request object.
    '''
    request_data = json.loads(request.get_data())
    server_logger.info(
        f"Client connection from: {request_data.get('client_name')}")
    server_logger.info(
        f"Client connection option: {request_data.get('option')}")
    server_logger.info(f"Client connection request: {request.get_url()}")
