import pandas as pd

from PIL import  Image
import os
import traceback

from src.core.utils.logger import log


def image_converter(input_path: str, output_format: str):
    try:
        base_name = os.path.splitext(input_path)[0]

        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'LA') and output_format.upper() in ('JPEG', 'JPG'):
                img = img.convert('RGB')
            
            output_path = f'{base_name}.{output_format.lower()}'

            img.save(output_path, output_format.upper())

    except Exception:
        log(f'{__file__} - {traceback.format_exc()}')