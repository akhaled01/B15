from utils.http.response_writer import HTTPResponseWriter
from utils.http.request_parser import HttpRequest
from utils.http.mux import Mux
from .server_logging import server_logger
import json
import socket
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

        response_data = Mux(request)  # route the request and get the result

        response_writer = HTTPResponseWriter(client_socket)
        response_writer.set_status_code(
            404) if response_data["message"] == "Not found" else response_writer.set_status_code(
            400) if response_data["message"] == "bad request" else response_writer.set_status_code(
                418) if response_data["message"] == "I like tea" else response_writer.set_status_code(
                    200)
        response_writer.add_header("Content-Type", "application/json")
        response_writer.set_content(json.dumps(response_data))
        response_writer.send_response()
    except Exception as e:
        response_writer.set_status_code(500)
        response_writer.send_response()
        server_socket.shutdown(2)
        server_socket.close()
        server_logger.critical(e)
        sys.exit(1)
