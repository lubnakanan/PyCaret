from pycaret.classification import setup, compare_models

def select_best_model(df):
    """
    Use PyCaret to automatically select the best machine learning model for the dataset.
    
    Args:
    - df (DataFrame): Input Pandas DataFrame containing the dataset.
    
    Returns:
    - best_model: Best trained machine learning model.
    """
    # Initialize PyCaret setup
    setup(data=df, target="Output")
    
    # Compare and select the best model
    best_model = compare_models()
    
    return best_model

# Example usage:
# best_model = select_best_model(df)
