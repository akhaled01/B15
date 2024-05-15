class HttpRequest:
    '''
      `HttpRequest` is a simple HTTP Request Parser.
      We parse the incoming raw data into requests, which we use
      to process the client further.

      The hypertext transport protocol is a standardized way of
      communicating over the www. SInce this TCP server is HTTP compliant, any client (eg: `python`, `JS`, `Go`, `curl`)
      can connect to it and make requests.
    '''

    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.data = None

    def parse_request(self, request_string):
        # Split request string into lines
        lines = request_string.splitlines()

        # Parse first line (method, URL, protocol)
        if lines:
            request_line = lines[0].split()
            if len(request_line) == 3:
                self.method = request_line[0]
                self.url = request_line[1]

        # Parse headers (key-value pairs)
        for line in lines[1:]:
            if line and ":" in line:
                header_key, header_value = line.split(":", 1)
                self.headers[header_key.strip()] = header_value.strip()

        # Check for data (assuming POST with Content-Length header)
        if "Content-Length" in self.headers:
            content_length = int(self.headers["Content-Length"])
            # Read data from the remaining bytes based on content length
            self.data = request_string.split("\r\n\r\n", 1)[1][:content_length]

    def get_method(self):
        return self.method

    def get_url(self):
        return self.url

    def get_headers(self):
        return self.headers

    def get_data(self):
        return self.data
