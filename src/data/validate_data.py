from src.data.loader import load_dataset


def main():
    df = load_dataset()
    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()