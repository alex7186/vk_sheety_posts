import json


def _get_config():
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/misc/config.json", "r") as f:
        data = f.read()
    return json.loads(data)


def _set_config(config):
    global SCRIPT_PATH
    with open(f"{SCRIPT_PATH}/misc/config.json", "w") as f:
        f.write(json.dumps(config, indent=4))
