from src.art.image import Image
from src.player.player_info import PlayerDirection
from typing import Dict


def get_image(direction: PlayerDirection):
    return Image.from_path(image_name=f"ConveyerBelt-{direction.name}.png")


CONVEYER_IMAGES: Dict[PlayerDirection, Image] = {
    direction: get_image(direction) for direction in PlayerDirection
}
