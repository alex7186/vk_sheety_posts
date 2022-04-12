import json
from vk_api import VkApi
import logging
import sys

SCRIPT_PATH = list(sys.argv)[1]
posts_collection = []


logging.basicConfig(
    filename=f"{SCRIPT_PATH}/misc/logfile.txt",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


def _get_config():
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/config.json", "r") as f:
        data = f.read()
    return json.loads(data)


def _set_config(config):
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/config.json", "w") as f:
        f.write(json.dumps(config, indent=4))


def get_next():
    global current_config
    current_config = _get_config()
    current_number = current_config["current_number"]
    current_config["current_number"] = current_number + 1
    _set_config(current_config)

    return current_number


def _load_post_collection():
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/misc/sheety.dump", "r") as f:
        return json.loads(f.read())


def get_post_by_number(number):
    """
    as count of posts may be less than input number
    the post id will be % with count of posts
    """

    posts_collection = _load_post_collection()

    return posts_collection[number % len(posts_collection)]


def get_sheety_content():
    current_number = get_next()
    sheety_title = f"Это уже {current_number} сообщение из моей специальной подборки для особого случая. Сгенерировано нейросетями.\n\n"

    return sheety_title + get_post_by_number(current_number)


def send_sheety_content():
    global current_config

    message = get_sheety_content()

    vk_session = VkApi(token=current_config["vk_api_249274091"])
    session_api = vk_session.get_api()

    for peer_id in current_config["peers_id"]:

        res = session_api.messages.send(random_id=0, peer_id=peer_id, message=message)
        logging.info(f"Message '{message[:20]}' sent to {peer_id} with id {res}")


send_sheety_content()
