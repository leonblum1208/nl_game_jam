from src.art.image import Image
from src.player.player_info import PlayerDirection
from typing import Dict


def get_image(direction: PlayerDirection, prefix: str, suffix: str = ".png"):
    return Image.from_path(image_name=f"{prefix}{direction.name}{suffix}")


BODOS_IMAGES: Dict[PlayerDirection, Image] = {
    direction: get_image(direction, prefix="Robo-") for direction in PlayerDirection
}

TURN_IMAGES: Dict[int, Image] = {
    -1: Image.from_path(image_name=f"Turn-LEFT.png"),
    1: Image.from_path(image_name=f"Turn-RIGHT.png"),
}

MOVE_IMAGES: Dict[int, Image] = {
    1: Image.from_path(image_name=f"move-FORWARD.png"),
    -1: Image.from_path(image_name=f"move-BACK.png"),
    0: Image.from_path(image_name=f"move-SLEEP.png"),
}
