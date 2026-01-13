import logging
import os

LOG_PATH = "logs"

def get_logger():
    os.makedirs(LOG_PATH, exist_ok=True)

    logging.basicConfig(
        filename=f"{LOG_PATH}/etl.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    return logging.getLogger()
