from src.art.image import Image
from src.grid.conveyer_direction import ConveyerDirection
from typing import Dict

def get_image(direction:ConveyerDirection):
    return Image.from_path(image_name=f"ConveyerBelt-{direction.name}.png")

CONVEYER_IMAGES: Dict[ConveyerDirection, Image] = {
    direction: get_image(direction) for direction in ConveyerDirection
}