def explore_data(df):
    """
    Perform exploratory data analysis (EDA) on the dataset.
    
    Args:
    - df (DataFrame): Input Pandas DataFrame.
    """
    # Display basic information about the dataset
    print("Basic information about the dataset:")
    print(df.info())
    
    # Display summary statistics for numerical columns
    print("\nSummary statistics for numerical columns:")
    print(df.describe())
    
    # Display the first few rows of the dataset
    print("\nFirst few rows of the dataset:")
    print(df.head())

# Example usage:
# explore_data(df)
