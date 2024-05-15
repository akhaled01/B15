from src.http.response_writer import HTTPResponseWriter
from src.http.request_parser import HttpRequest
from .utils.server_logging import server_logger
from .utils.client_logging import LogClientRequest, LogClientConn
from src.http.mux import Router
import threading
import socket
import json
import sys


def HandleClient(client_socket: socket.socket, server_socket: socket.socket):
    '''
      `HandleClient` is the main function that handles the client connection.
      It receives the client socket and parses the request.
      Then it routes the request to the appropriate controller.
      Finally, it sends the response back to the client.

      Parameters:
      client_socket (socket): The client socket.

      Returns:
      None
    '''
    try:
        raw_data = client_socket.recv(2048)
        request = HttpRequest()
        request.parse_request(raw_data.decode('utf-8'))

        LogClientConn(request)

        response_data = Router(request)

        response_writer = HTTPResponseWriter(client_socket)
        match response_data["message"]:
            case "Not found":
                response_writer.set_status_code(404)
            case "bad request":
                response_writer.set_status_code(400)
            case "I like tea":
                response_writer.set_status_code(418)
            case _:
                response_writer.set_status_code(200)

        response_writer.add_header("Content-Type", "application/json")
        response_writer.set_content(json.dumps(response_data))
        response_writer.send_response()

        LogClientRequest(
            request=request, response_data=response_data, response_writer=response_writer)

    except Exception as e:
        response_writer.set_status_code(500)
        response_writer.send_response()

        server_socket.shutdown(2)
        server_socket.close()

        server_logger.critical(
            f"Error while handling client thread: {threading.current_thread().name}")
        server_logger.print_exception(e)
        sys.exit(1)