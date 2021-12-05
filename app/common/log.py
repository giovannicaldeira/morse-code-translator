from logging import StreamHandler, Formatter, getLogger
from os import getenv


STREAM_HANDLER = StreamHandler()
STREAM_HANDLER.setFormatter(
    Formatter(
        "[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)s] %(message)s",
        datefmt="%Y-%m-%d%T%H:%M:%S",
    )
)


class Logger:
    def __init__(self, module: str):
        self.logger = getLogger(module)
        self.logger.setLevel(getenv("LOG_LEVEL", "INFO"))
        self.logger.addHandler(STREAM_HANDLER)

    def getLogger(self):
        return self.logger