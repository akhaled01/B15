from src.controllers.headlines import GetHeadlines
from src.controllers.sources import GetSources
import json


def Router(req) -> dict:
    '''
      `Router` is a simple Routing multiplexer. It takes in a `HttpRequest` object and 
      returns a string. The string is the response to be sent back to the client.

      It is used to route the request to the appropriate controller.

      Parameters:
      req (HttpRequest): The request object.

      Returns:
      dict: The response to be sent back to the client.
    '''
    if req.get_url() == "/":
        return {"message": "Hello!"}

    elif req.get_url() == "/headlines":
        if not req.get_data():
            return {"message": "bad request"}
        request_data = json.loads(req.get_data())
        return {"message": GetHeadlines(request_data.get("keywords"),
                                        request_data.get("country"),
                                        request_data.get("category"))}

    elif req.get_url() == "/sources":
        if not req.get_data():
            return {"message": "bad request"}
        request_data = json.loads(req.get_data())
        return {"message": GetSources(request_data.get("country"),
                                      request_data.get("category"),
                                      request_data.get("lang"))}

    elif req.get_url() == "/tea":
        return {"message": "I like tea"}  # tea is cool :)

    return {"message": "Not found"}
