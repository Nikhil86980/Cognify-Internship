"""
Level 3 - Task 2: Create a Data Visualization Tool
Takes a dataset and generates visualizations using Matplotlib and Seaborn.

Install requirements first:
    pip install matplotlib seaborn pandas

We use a small built-in sample dataset (monthly sales) so this runs
without needing to download anything.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_dataset():
    # In a real project you'd load a CSV with: pd.read_csv("yourfile.csv")
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [12000, 15000, 11000, 18000, 20000, 17000],
        "Expenses": [8000, 9000, 8500, 10000, 11000, 9500]
    }
    return pd.DataFrame(data)


def visualize_data(df):
    sns.set_theme(style="darkgrid")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Line chart: Sales vs Expenses over time
    axes[0].plot(df["Month"], df["Sales"], marker="o", label="Sales")
    axes[0].plot(df["Month"], df["Expenses"], marker="o", label="Expenses")
    axes[0].set_title("Sales vs Expenses by Month")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Amount ($)")
    axes[0].legend()

    # Bar chart: Sales by month
    sns.barplot(x="Month", y="Sales", data=df, ax=axes[1], hue="Month", legend=False)
    axes[1].set_title("Monthly Sales")

    plt.tight_layout()
    plt.savefig("sales_visualization.png")
    print("Chart saved as 'sales_visualization.png'")
    plt.show()


if __name__ == "__main__":
    df = create_sample_dataset()
    print("Dataset preview:")
    print(df)
    visualize_data(df)
