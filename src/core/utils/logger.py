import os
import logging


appdata_path = os.getenv('APPDATA')
logs_dir = os.path.join(appdata_path, 'automation', 'logs')

os.makedirs(logs_dir, exist_ok=True)

log_file = os.path.join(logs_dir, 'automation.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)


def log(message: str):
    logging.info(message)
