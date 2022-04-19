import pandas as pd
from vk_api import VkApi
import json


def download_posts(token, count100=20, filename="time_dump.dump"):
    vk_session = VkApi(token=token)

    # Для вызова методов vk_api session_api
    session_api = vk_session.get_api()

    input_array = []
    for i in range(count100):
        input_array.append(
            session_api.wall.get(domain="neuralshit", offset=i * 100, count=100)
        )

    array_clean = []
    for input_subarray in input_array:
        for post in input_subarray["items"]:
            array_clean.append(
                {"id": post["id"], "date": post["date"], "text": post["text"]}
            )

    posts_count = len(array_clean)

    df_array_clean = pd.DataFrame(array_clean)
    df_array_clean["date"] = pd.to_datetime(df_array_clean["date"], unit="s")
    df_array_clean["wendsday"] = df_array_clean.date.apply(filter_dow_2)
    df_array_clean["startquote"] = df_array_clean.text.apply(filter_quote_start)
    df_array_clean["target_post"] = (
        df_array_clean["wendsday"] * df_array_clean["startquote"]
    )

    df_array_clean = df_array_clean[df_array_clean["target_post"] > 0]
    df_array_clean.text = df_array_clean.text.apply(filter_replace_quote_arrow)

    time_dump = dict(
        {
            "last_date_timestamp_value": max(df_array_clean.date).value,
            "posts_count": posts_count,
            "data": tuple(df_array_clean.text),
        }
    )

    with open(filename, "w") as f:
        f.write(json.dumps(time_dump))

    return time_dump


def filter_dow_2(x):
    return 1 if x.dayofweek == 2 else 0


def filter_quote_start(x):
    return 1 if "»" in x else 0


def filter_replace_quote_arrow(x):
    return x[x.find("\n»") :].replace("»", "-> ")
