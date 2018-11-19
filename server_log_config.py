import logging
import sys

logging.basicConfig(
    filename = "info.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.DEBUG
)

app_log = logging.getLogger('app')
app_log.setLevel(logging.DEBUG)
app_log.propagate = False
app_log.addHandler(logging.FileHandler('info.log'))
app_log.addHandler(logging.StreamHandler(sys.stderr))
app_log.info('help')
