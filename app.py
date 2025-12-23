import logging
from flask import Flask, request
from pythonjsonlogger import jsonlogger

app = Flask(__name__)

# ----- JSON Logger Setup -----
logger = logging.getLogger("happy-hive")
logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s %(remote_addr)s"
)
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
app.logger = logger
# --------------------------------

@app.route("/")
def home():
    app.logger.info(
        "Homepage accessed Emine",
        extra={"remote_addr": request.remote_addr}
    )
    return "Hello from Flask behind Nginx!"
