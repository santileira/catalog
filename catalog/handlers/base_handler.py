import jsonpickle
from tornado.web import RequestHandler

import logging

from catalog.error.api_error_response import APIErrorResponse

logger = logging.getLogger(__name__)


class BaseHandler(RequestHandler):

    def data_received(self, chunk):
        """
        it is only to implement all abstract methods
        """
        pass

    def set_default_headers(self) -> None:
        """Set the default response header to be JSON."""
        self.set_header("Content-Type", 'application/json; charset="utf-8"')

    def send_response(self, response, status: int) -> None:
        """Construct and send a JSON response with appropriate status code."""
        self.set_status(status)
        self.write(jsonpickle.encode(response, unpicklable=False))

    def send_error_response(self, api_error: APIErrorResponse) -> None:
        """Construct and send a error JSON response with appropriate status code."""
        self.send_response(api_error, api_error.status_code)
