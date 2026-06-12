from src.data.loader import load_dataset


def test_dataset_loads():

    df = load_dataset()

    assert df is not None


def test_dataset_not_empty():

    df = load_dataset()

    assert len(df) > 0