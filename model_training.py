from sklearn.model_selection import train_test_split

def train_model(df):
    """
    Train a machine learning model using the dataset.
    
    Args:
    - df (DataFrame): Input Pandas DataFrame containing the dataset.
    
    Returns:
    - model: Trained machine learning model.
    """
    # Split the data into features (X) and target variable (y)
    X = df.drop(columns=["Output"])
    y = df["Output"]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Placeholder for model training code
    # Replace this with your actual model training code
    
    return model

# Example usage:
# model = train_model(df)
