from .response_parser import HttpResponseParser
import socket
import json


class ClientHttpRequest:
    '''
      `CLientHttpRequest` is a class that represents an HTTP request from the client.
      It takes in the request data and parses it.
      It then returns the parsed data.
      It also sends the request to the server.
    '''

    def __init__(self) -> HttpResponseParser:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 9090

    def send(self, data):
        try:
            self.sock.connect((self.host, self.port))
            self.sock.send(data)
            raw_response = self.sock.recv(4096).decode('utf-8')
            return HttpResponseParser(raw_response)
        except BrokenPipeError:
            # Handle broken pipe error (e.g., log error or return appropriate value)
            print(
                f"BrokenPipeError: Failed to receive response from server {self.host}:{self.port}")
            return None
        finally:
            self.sock.close()

    def GET(self, uri: str, data: dict = None):
        '''
          This method sends a GET request to the server.

          Params:
              uri (str): The URL of the resource to request.
              host (str): The host of the server.
              data (dict): The data to send to the server (optional).

          Returns:
                  `HTTPResponseParser`: The response from the server.
        '''
        if data:
            data_str = json.dumps(data)
            content_length = len(data_str.encode('utf-8'))
            self.request = f"""GET {uri} HTTP/1.1\r\nHost: {self.host}:{self.port}\r\nContent-Length: {content_length}\r\n\r\n{data_str}"""
            print(self.request)
        else:
            self.request = f"GET {uri} HTTP/1.1\r\nHost: {self.host}:{self.port}\r\n\r\n"
        return self.send(self.request.encode('utf-8'))

    def POST(self, url: str, host: str, port: int, data: dict):
        '''
          This method sends a POST request to the server.

          Params:
              url (str): The URL of the resource to request.
              host (str): The host of the server.
              port (int): The port of the server (optional).
              data (dict): The data to send to the server.

          Returns:
                  str: The response from the server.
        '''
        if port:
            host_with_port = f"{host}:{port}"
        else:
            host_with_port = host

        data_str = json.dumps(data)
        content_length = len(data_str.encode('utf-8'))
        self.request = f"""POST {url} HTTP/1.1\r\nHost: {host_with_port}\r\nContent-Type: application/json\r\nContent-Length: {content_length}\r\nConnection: close\r\n\r\n{data_str}"""
        return self.send(self.request.encode('utf-8'))
