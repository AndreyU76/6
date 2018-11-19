import logging
import sys
import logging.handlers


logging.basicConfig(
    filename = "info.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.DEBUG
)


app_log = logging.getLogger('app')
app_log.setLevel(logging.DEBUG)
app_log.propagate = False
app_log.addHandler(logging.FileHandler('info.log'))
handlers = logging.handlers.RotatingFileHandler('info.log', encoding='utf8', maxBytes=100000, logging.StreamHandler())
handlers = logging.handlers.TimedRotatingFileHandler(info, when='D', interval=1)
