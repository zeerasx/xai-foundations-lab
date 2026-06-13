import matplotlib.pyplot as plt
import seaborn as sns


def plot_target_distribution(df, target_col):
    """
    Plot target distribution.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[target_col], kde=True)
    plt.title(f"Distribution of {target_col}")
    plt.tight_layout()
    plt.show()


def plot_feature_distributions(df):
    """
    Plot all feature distributions.
    """
    df.hist(
        figsize=(15, 10),
        bins=30,
        edgecolor="black"
    )
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df):
    """
    Plot correlation heatmap.
    """
    plt.figure(figsize=(10, 8))

    corr = df.corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()


def plot_feature_vs_target(df, target_col):
    """
    Scatter plots of features vs target.
    """

    features = [
        col for col in df.columns
        if col != target_col
    ]

    rows = 3
    cols = 3

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(15, 12)
    )

    axes = axes.flatten()

    for idx, feature in enumerate(features):

        sns.scatterplot(
            x=df[feature],
            y=df[target_col],
            ax=axes[idx]
        )

        axes[idx].set_title(
            f"{feature} vs {target_col}"
        )

    plt.tight_layout()
    plt.show()