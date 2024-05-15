def validate_data(data) -> bool:
    """
    `validate_data` is a function that validates the data sent by the client.
    It takes in a dictionary of data and returns a boolean.
    The boolean is used to determine if the data is valid.
    """
    if data.get("client_name") is None or data.get("option") is None:
        return False
      