from .utils.client_logging import LogClientRequest, LogClientConn
from .http.response_writer import HTTPResponseWriter
from .utils.server_logging import server_logger
from .http.request_parser import HttpRequest
from .http.router import Router
import threading
import socket
import json
import traceback


def HandleClient(client_socket: socket.socket):
    '''
      `HandleClient` is the main function that handles the client connection.
      It receives the client socket and parses the request.
      Then it routes the request to the appropriate controller.
      Finally, it sends the response back to the client.

      This function handles exceptions gracefully and logs the request and response.

      Parameters:
      client_socket (socket): The client socket.

      Returns:
      None
    '''
    try:
        try:
            raw_data = client_socket.recv(4096)
        except OSError:
            pass
        print("recv data")
        print(raw_data.decode('utf-8'))
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
            case "Client Registered":
                response_writer.set_status_code(201)
            case "Unauthorized":
                response_writer.set_status_code(401)
            case "Method not allowed":
                response_writer.set_status_code(405)
            case "This name already exists":
                response_writer.set_status_code(409)
            case _:
                response_writer.set_status_code(200)

        response_writer.add_header("Content-Type", "application/json")
        response_writer.set_content(
            json.dumps(response_data))
        response_writer.send_response()

        LogClientRequest(
            request=request, response_writer=response_writer)

        client_socket.close()

    except Exception as e:
        try:
            server_logger.error(traceback.format_exc())
        except Exception as send_error:
            server_logger.error(f"Error sending response: {send_error}")

        server_logger.critical(
            f"Error while handling client thread: {threading.current_thread().name} -> {e}")
