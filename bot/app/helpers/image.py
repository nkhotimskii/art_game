import os

from aiogram.types import FSInputFile

from constants import IMAGES_FOLDER


def get_image(image_name: str) -> FSInputFile:
    image_path = os.path.join(IMAGES_FOLDER, image_name)
    return FSInputFile(image_path)