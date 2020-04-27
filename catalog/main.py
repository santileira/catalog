import logging
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from catalog.handlers import JobSeriesHandler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(name)s: %(message)s')
logging.getLogger('tornado.access').disabled = True
logger = logging.getLogger(__name__)


class Main:

    def start_application(self):
        app = self.create_app()
        http_server = HTTPServer(app)
        http_server.listen(5005)
        logger.info("Starting Catalog server on port: 5005")
        IOLoop.current().start()

    @staticmethod
    def create_app() -> Application:
        app = Application([
            ('/job/series', JobSeriesHandler)
        ])

        return app


def main():
    main = Main()
    main.start_application()


if __name__ == '__main__':
    main()
