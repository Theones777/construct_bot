from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN")
    CHEF_TG_ID = getenv("CHEF_TG_ID")
    CHEF_NUMBER = getenv("CHEF_NUMBER", "+7 123 456-78-99")

    ORDER_STRUCTURE_PATH = "data/order_structure.json"
    IMAGES_PATH = "data/imgs"
    IMG_MAX_SIZE = (800, 600)
    IMG_CROP_MODE = "hard_resize"
    STEPS_NAMES = {
            "слои": "слоёв",
            "начинка": "начинок",
            "тип": "типов",
        }