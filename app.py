import logging
import os

from back.config_manager import get_config
from back.sheety_content_manager import send_sheety_content

SCRIPT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-1])
posts_collection = []


logging.basicConfig(
    filename=f"{SCRIPT_PATH}/misc/logfile.txt",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

current_config = get_config(SCRIPT_PATH)
send_sheety_content(current_config=current_config, SCRIPT_PATH=SCRIPT_PATH)
