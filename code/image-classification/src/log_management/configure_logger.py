import logging
from logging.config import fileConfig


def setup_logger(log_config_file_path: str):
    fileConfig(log_config_file_path, defaults={"logfilename": "logs/app.log"})
    logger = logging.getLogger()
    logger.info(f"Logfile creation done.")
