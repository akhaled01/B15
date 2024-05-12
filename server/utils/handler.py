from utils.logging import server_logger
from utils.http.response_writer import HTTPResponseWriter
from utils.http.request_parser import HttpRequest


def handle_client(client_socket):
    raw_data = client_socket.recv(2048)
    request = HttpRequest()
    request.parse_request(raw_data.decode())

    response_writer = HTTPResponseWriter(client_socket)
    response_writer.set_status_code(200)
    response_writer.add_header("Content-Type", "text/plain")
    response_writer.set_content("Hello!")
    response_writer.send_response()
    client_socket.close()
