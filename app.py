import json
from vk_api import VkApi
import logging
import os

SCRIPT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-1])
print(SCRIPT_PATH)
posts_collection = []


logging.basicConfig(
    filename=f"{SCRIPT_PATH}/misc/logfile.txt",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


def _get_config():
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/misc/config.json", "r") as f:
        data = f.read()
    return json.loads(data)


def _set_config(config):
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/misc/config.json", "w") as f:
        f.write(json.dumps(config, indent=4))


def _get_vk_key(SCRIPT_PATH):
    with open(f"{SCRIPT_PATH}/vk_key.txt", "r") as f:
        return f.read()


def set_next_number(current_config):
    current_number = current_config["current_number"]
    current_config["current_number"] = current_number + 1
    _set_config(current_config)

    return current_number


def _load_post_collection(SCRIPT_PATH):
    with open(f"{SCRIPT_PATH}/misc/sheety.dump", "r") as f:
        return json.loads(f.read())


def get_post_by_number(number, SCRIPT_PATH):
    """
    as count of posts may be less than input number
    the post id will be % with count of posts
    """

    posts_collection = _load_post_collection(SCRIPT_PATH)

    return posts_collection[number % len(posts_collection)]


def get_sheety_content(SCRIPT_PATH, current_config):
    current_number = set_next_number(current_config=current_config)
    sheety_title = f"Это уже {current_number} сообщение из моей специальной подборки для особого случая. Сгенерировано нейросетями.\n\n"

    return sheety_title + get_post_by_number(
        number=current_number, SCRIPT_PATH=SCRIPT_PATH
    )


def send_sheety_content(current_config, SCRIPT_PATH):
    message = get_sheety_content(SCRIPT_PATH=SCRIPT_PATH, current_config=current_config)

    vk_session = VkApi(token=_get_vk_key(SCRIPT_PATH))
    session_api = vk_session.get_api()

    for peer_id in current_config["peers_id"]:

        res = session_api.messages.send(random_id=0, peer_id=peer_id, message=message)
        logging.info(f"Message '{message[:20]}' sent to {peer_id} with id {res}")


current_config = _get_config()
send_sheety_content(current_config=current_config, SCRIPT_PATH=SCRIPT_PATH)
