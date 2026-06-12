from sklearn.datasets import fetch_california_housing
import pandas as pd

from src.utils.logger import setup_logger


logger = setup_logger()


def load_dataset() -> pd.DataFrame:
    """
    Load California Housing dataset.

    Returns
    -------
    pd.DataFrame
        Dataset as pandas dataframe.
    """

    logger.info("Loading California Housing dataset")

    housing = fetch_california_housing(as_frame=True)

    df = housing.frame

    logger.info(
        f"Dataset loaded successfully. Shape={df.shape}"
    )

    return df