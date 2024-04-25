import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
    - file_path (str): Path to the CSV file.
    
    Returns:
    - df (DataFrame): Pandas DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
        return None

# Example usage:
df = load_data("C:\\Users\\User\\Downloads\\archive (8)\\onlinefoods.csv")
