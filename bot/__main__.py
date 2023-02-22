import logging

from .utubebot import UtubeBot
from .config import Config


if utubebot == "__main__":
    logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
    logging.getLogger("pyrogram").setLevel(
        logging.INFO if Config.DEBUG else logging.WARNING
    )

    UtubeBot().run()
