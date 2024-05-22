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

    def __init__(self, sock: socket.socket) -> HttpResponseParser:
        self.sock = sock

    def send(self, data):
        print(socket.fil)
        self.sock.sendall(data)
        return HttpResponseParser(self.sock.recv(4096).decode('utf-8'))

    def GET(self, url: str, host: str, data: dict = None):
        '''
          This method sends a GET request to the server.

          Params:
              url (str): The URL of the resource to request.
              host (str): The host of the server.
              data (str): The data to send to the server.

          Returns:
                  str: The response from the server.
        '''
        self.request = f"GET {url} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n{data}"
        return self.send(self.request.encode('utf-8'))

    def POST(self, url: str, host: str, data: dict):
        '''
          This method sends a POST request to the server.

          Params:
              url (str): The URL of the resource to request.
              host (str): The host of the server.
              data (str): The data to send to the server.

          Returns:
                  str: The response from the server.
        '''
        self.request = f"""POST {url} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/json\r\nContent-Length: {len(data)}\r\nConnection: close\r\n\r\n
        {json.dumps(data)}"""
        return self.send(self.request.encode('utf-8'))
