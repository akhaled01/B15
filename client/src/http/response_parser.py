class HttpResponseParser:
    '''
      This class parses the response data from the server and returns the response body.
      It takes in the response data and parses the response.
      It then returns the response body.
    '''

    def __init__(self, response_data: str):
        self.response_data = response_data
        self.headers = {}
        self.body = None
        self.status_code = 200
        self.reason_phrase = "OK"
        self.version = "HTTP/1.1"
        self._parse_response()

    def _parse_response(self):
        print(self.response_data)
        try:
            header_data, self.body = self.response_data.split('\r\n\r\n', 1)
        except ValueError:
            print("Error: Could not parse response")
            return
        headers = header_data.split('\r\n')
        status_line = headers[0]
        self.version, self.status_code, self.reason_phrase = status_line.split(
            ' ', 2)
        for header in headers[1:]:
            key, value = header.split(':', 1)
            self.headers[key.strip()] = value.strip()

    def get_header(self, header_name):
        return self.headers.get(header_name)

    def get_body(self):
        return self.body

    def get_status_code(self):
        return int(self.status_code)

    def get_reason_phrase(self):
        return self.reason_phrase
