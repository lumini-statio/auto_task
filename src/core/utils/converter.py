import pandas as pd

from PIL import Image
import os
import traceback
import sqlite3

from src.core.utils.logger import log


def image_converter(input_path: str, output_format: str):
    try:
        base_name = os.path.splitext(input_path)[0]

        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'LA') \
                and output_format.upper() \
                    in ('JPEG', 'JPG'):
                img = img.convert('RGB')

            output_path = f'{base_name}.{output_format.lower()}'

            img.save(output_path, output_format.upper())

    except Exception:
        log(f'{__file__} - {traceback.format_exc()}')


def file_converter(
        input_path,
        input_format: str,
        output_path,
        output_format: str,
        sep: str = ','
        ):
    file = None

    con = sqlite3.Connection(output_path)

    match input_format:
        case 'csv':
            file = pd.read_csv(input_path, sep=sep)
        case 'json':
            file = pd.read_json(input_path)
        case 'excel':
            file = pd.read_excel(input_path)
        case 'sql':
            file = pd.read_sql(input_path, con=con)

    match output_format:
        case 'json':
            file.to_json(output_path, index=False, orient='records', indent=4)
        case 'csv':
            file.to_csv(output_path, index=False)
        case 'excel':
            file.to_excel(output_path, index=False)
        case 'sql':
            file.to_sql(
                con=con,
                name='data',
                if_exists='replace',
                index=False
            )
