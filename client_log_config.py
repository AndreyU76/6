import logging
import sys

logging.basicConfig(
    filename = "client.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
logger.critical('DEBUG')
