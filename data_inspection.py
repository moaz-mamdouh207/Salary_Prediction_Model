import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def print_categorical_value_counts(df: pd.DataFrame) -> None:
    """
    Prints the name of each categorical column in the DataFrame along with its value counts.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
        
    Returns
    -------
    None
        Prints the value counts for each categorical column directly.
    """
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    for col in categorical_cols:
        print(df[col].value_counts())
        print("_"*50)
        print("_"*50)

def plot_salary_by_experience(df):
    """
    Plot salary distribution across experience groups using boxplots.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataframe containing experience and salary columns.

    Notes
    -----
    - Bins experience into groups (0-5, 5-10, ..., 25-30).
    """
    # Define bins and labels
    bins = [0, 5, 10, 15, 20, 25, 30]
    labels = ["0-5", "5-10", "10-15", "15-20", "20-25", "25-30"]

    # Bin experience values into categories (without modifying df)
    exp_groups = pd.Categorical(
        pd.cut(df["Experience"], bins=bins, labels=labels, include_lowest=True),
        categories=labels, ordered=True
    )

    # Plot with seaborn
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=exp_groups, y=df["Salary"], palette="husl", hue=exp_groups)
    plt.title("Salary Distribution by Experience Group", fontsize=14)
    plt.xlabel("Experience Group (years)")
    plt.ylabel("Salary")
    plt.show()
