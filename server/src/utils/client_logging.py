from .server_logging import server_logger
from src.http.response_writer import HTTPResponseWriter
from src.http.request_parser import HttpRequest
from datetime import datetime
import json


def LogClientRequest(request: HttpRequest, response_writer: HTTPResponseWriter):
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
    data = json.loads(request.get_data()) if request.get_data() else None
    if not data:
        return

    if type(data) is not dict:
        data = json.loads(data)

    with open(f"log/json/B15_{data.get('client_name')}_{data.get('option')}.json", "w") as f:
        f.write(json.dumps({
            "client_name": data.get("client_name"),
            "option": data.get("option"),
            "response_status": str(response_writer.status_code) + " " + response_writer._get_status_message(response_writer.status_code),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "response": response_writer.get_response_data()
        }))


def LogClientConn(request: HttpRequest):
    '''
      `LogClientConn` is a function that logs the client connection.
      It takes in the `HttpRequest` object and the client socket.
      It then logs the request and response to the terminal.

      Parameters:
      request (HttpRequest): The request object.
    '''

    try:
        request_data = json.loads(request.get_data())

        if type(request_data) is not dict:
            request_data = json.loads(request_data)

        server_logger.info(
            f"Client connection from: {request_data.get('client_name')}")
        server_logger.info(
            f"Client connection option: {request_data.get('option')}") if request_data.get("option") else None
        server_logger.info(
            f"Client connection request: {request.get_url()}") if request.get_url() else None
    except Exception as e:
        server_logger.error(f"Error logging client connection: {e}")
        return
