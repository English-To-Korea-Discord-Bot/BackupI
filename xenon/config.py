from os import environ as env
import logging

log = logging.getLogger(__name__)


class Config:
    token = None
    shard_count = 1
    per_cluster = 1

    prefix = "k!"

    dbl_token = None

    support_guild = 918805032298745926
    owner_id = 932290636013518899
    invite_url = None  # Set to None to generate one automatically

    identifier = "BackupI"

    db_host = "localhost"
    db_user = None
    db_password = None

    redis_host = "localhost"

    template_approval = 633228946875482112
    template_list = 633228950998614037
    template_featured = 633228948251082752

    extensions = [
        "errors",
        "help",
        "admin",
        "backups",
        "templates",
        "users",
        "basics",
        "sharding",
        "botlist",
        "api",
        "builder"
    ]


def __getattr__(name):
    default = getattr(Config, name, None)
    value = env.get(name.upper())

    if value is not None:
        if isinstance(default, int):
            return int(value)

        if isinstance(default, float):
            return float(value)

        if isinstance(default, bool):
            valid = ["y", "yes", "true"]
            return value.lower() in valid

        if isinstance(default, list):
            return value.split(",")

        return value

    return default
