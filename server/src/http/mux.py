from src.controllers.headlines import GetHeadlines
import json


def Mux(req) -> dict:
    '''
      `Mux` is a simple multiplexer. It takes in a `HttpRequest` object and 
      returns a string. The string is the response to be sent back to the client.

      The multiplexer is used to route the request to the appropriate controller.
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
    elif req.get_url() == "/tea":
        return {"message": "I like tea"}
    return {"message": "Not found"}
