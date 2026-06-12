import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def setup_logger():
    """
    Configure project logger.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger("xai_lab")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_DIR / "project.log"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger