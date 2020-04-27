class APIErrorResponse:
    """
    APIErrorResponse class is the representation of an api error in our system.
    For example, bad request error, internal server error, not found error, etc.
    It has three attributes: the message, the cause and the status code.
    """

    def __init__(self, message: str, cause: str, status_code: int) -> None:
        self.message = message
        self.cause = cause
        self.status_code = status_code
