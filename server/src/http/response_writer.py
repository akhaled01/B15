class HTTPResponseWriter:
    """
    Provides a simple HTTP response writer that can be used to send responses to
    clients connected to the server.

    The `HTTPResponseWriter` class is responsible for constructing and sending
    HTTP responses back to the client. It allows setting the status code, adding
    headers, and setting the response content.
    """

    def __init__(self, client_socket):
        self.client_socket = client_socket
        self.status_code = 200
        self.headers = {}
        self.content = b""

    def set_status_code(self, code):
        self.status_code = code

    def add_header(self, key, value):
        self.headers[key] = value

    def set_content(self, content):
        self.content = content.encode('ascii')

    def send_response(self):
        """
          Constructs the HTTP response header string with the status code and status message.

          Args:
              self (object): The current instance of the class.

          Returns:
              str: The HTTP response header string.
          """
        response = f"HTTP/1.1 {self.status_code} {self._get_status_message(self.status_code)}\r\n"
        for key, value in self.headers.items():
            response += f"{key}: {value}\r\n"
        response += "\r\n"
        response += self.content.decode("utf-8")
        self.client_socket.sendall(response.encode('utf-8'))

    def _get_status_message(self, code):
        # Maps status codes to messages (add more as needed)
        messages = {
            200: "OK",
            404: "Not Found",
            400: "Bad Request",
            500: "Internal Server Error",
            405: "Method Not Allowed",
            418: "I'm a teapot",
        }
        return messages.get(code, "Unknown Status Code")
