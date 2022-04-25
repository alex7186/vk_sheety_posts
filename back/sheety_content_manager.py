import json
from vk_api import VkApi
import logging

from back.config_manager import set_config
from back.token_manager import get_token


def set_next_number(current_config, SCRIPT_PATH):
    current_number = current_config["current_number"]
    current_config["current_number"] = current_number + 1
    set_config(config=current_config, SCRIPT_PATH=SCRIPT_PATH)

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
    current_number = set_next_number(
        current_config=current_config,
        SCRIPT_PATH=SCRIPT_PATH,
    )
    sheety_title = f"Это уже {current_number} сообщение из моей специальной подборки для особого случая. Сгенерировано нейросетями.\n\n"

    return sheety_title + get_post_by_number(
        number=current_number, SCRIPT_PATH=SCRIPT_PATH
    )


def send_sheety_content(current_config, SCRIPT_PATH):
    message = get_sheety_content(SCRIPT_PATH=SCRIPT_PATH, current_config=current_config)

    vk_session = VkApi(token=get_token(SCRIPT_PATH))
    session_api = vk_session.get_api()

    for peer_id in current_config["peers_id"]:

        res = session_api.messages.send(random_id=0, peer_id=peer_id, message=message)
        logging.info(f"Message '{message[:20]}' sent to {peer_id} with id {res}")
