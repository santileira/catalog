import asyncio
import logging
from http import HTTPStatus

from catalog.series.async_scrapper import main
from .base_handler import BaseHandler

logger = logging.getLogger(__name__)


class JobSeriesHandler(BaseHandler):
    """Only allow POST, GET, PATCH, DELETE requests."""

    SUPPORTED_METHODS = ["POST"]

    def post(self) -> None:
        try:
            asyncio.run(main())
            self.send_response({"response": "training successful"}, HTTPStatus.CREATED)

        except Exception as ex:
