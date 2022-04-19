import os

from back.token_manager import get_token
from back.download_manager import download_posts

SCRIPT_PATH = "/".join(os.path.realpath(__file__).split("/")[:-1])
output_filename = "./misc/time_dump.dump"

download_posts(token=get_token(SCRIPT_PATH), filename=output_filename)

print(f"created file in {output_filename}")
