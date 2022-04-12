import json
from crontab import CronTab
import sys

args = list(sys.argv)[1:]

with open("./config.json", "r") as f:
    config_data = json.load(f)
    SCRIPT_PATH = config_data["SCRIPT_PATH"]
    APP_NAME = config_data["APP_NAME"]

if "start" in args:
    cron = CronTab(user=True)

    for existing_job in cron:
        if existing_job.comment == APP_NAME:
            cron.remove(existing_job)

    job = cron.new(
        command=f"python3 {SCRIPT_PATH}/app.py {SCRIPT_PATH}", comment=APP_NAME
    )
    job.setall(30, 8, None, None, "3-5")

    cron.write()

elif "stop" in args:
    cron = CronTab(user=True)

    for existing_job in cron:
        if existing_job.comment == APP_NAME:
            cron.remove(existing_job)

    cron.write()
