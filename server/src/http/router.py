from src.controllers.headlines import GetHeadlines
from src.controllers.sources import GetSources
from src.http.request_parser import HttpRequest
from ..utils.server_logging import server_logger
from threading import Lock
import json

ONLINE_CLIENTS = []
ONLINE_CLIENT_MUTEX = Lock()


'''
  A tiny explanation of the mutex:
  The mutex is used to prevent race conditions.
  If there are multiple threads trying to access the same resource (the array of online clients),
  the mutex ensures that only one thread can access the resource at a time.
'''


def Router(req: HttpRequest) -> dict:
    '''
      `Router` is a simple Routing multiplexer. It takes in a `HttpRequest` object and
      returns a string. The string is the response to be sent back to the client.

      It is used to route the request to the appropriate controller.

      Parameters:
      req (HttpRequest): The request object.

      Returns:
      dict: The response to be sent back to the client.
    '''
    if not req.get_data():
        return {"message": "bad request"}

    request_data = json.loads(req.get_data())

    if type(request_data) is not dict:
        request_data = json.loads(request_data)

    if req.get_url() == "/":  # test
        return {"message": "Hello!"}

    elif req.get_url() == "/headlines":  # client requests headlines
        with ONLINE_CLIENT_MUTEX:
            if not request_data.get("client_name") or request_data.get("client_name") not in ONLINE_CLIENTS:
                return {"message": "Unauthorized"}

            server_logger.info(
                f"""Client request headlines: {request_data.get('client_name')},
            {request_data.get('keywords')}, {request_data.get('country')},
            {request_data.get('category')}""")

            return {"message": GetHeadlines(request_data.get("keywords"),
                                            request_data.get("country"),
                                            request_data.get("category"))}

    elif req.get_url() == "/sources":  # client requests sources
        with ONLINE_CLIENT_MUTEX:
            if request_data.get("client_name") not in ONLINE_CLIENTS:
                return {"message": "Unauthorized"}

            res = GetSources(request_data.get("country"),
                             request_data.get("category"),
                             request_data.get("lang"))

            server_logger.info(
                f"""Client request sources: {request_data.get('client_name')},
            {request_data.get('country')}, {request_data.get('category')},
            {request_data.get('lang')}""")

            return {"message": res}

    elif req.get_url() == "/conn":  # client connection
        if req.get_method() != "POST":
            return {"message": "Method not allowed"}

        name = request_data.get("client_name")

        with ONLINE_CLIENT_MUTEX:
            if name in ONLINE_CLIENTS:
                return {"message": f"This name already exists"}

            ONLINE_CLIENTS.append(name)

        server_logger.info(
            f"Client conn: {name}")

        return {"message": "Client Registered"}

    elif req.get_url() == "/disconn":  # client disconnection
        if req.get_method() != "POST":
            return {"message": "Method not allowed"}

        name = request_data.get("client_name")

        with ONLINE_CLIENT_MUTEX:
            if name not in ONLINE_CLIENTS:
                return {"message": "Unauthorized"}

        ONLINE_CLIENTS.remove(name)

        server_logger.info(
            f"Client disconn: {name}")

        return {"message": "Client Disconnected"}

    elif req.get_url() == "/tea":
        return {"message": "I like tea"}  # tea is cool :)

    return {"message": "Not found"}
