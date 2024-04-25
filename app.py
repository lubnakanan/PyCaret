import streamlit as st

def main():
    """
    Main function to create the Streamlit web app.
    """
    st.title("Online Food Order Analysis")
    
    # Sidebar for uploading file
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Load data
        df = pd.read_csv(uploaded_file)
        
        # Display basic information about the dataset
        st.write("Basic information about the dataset:")
        st.write(df.info())
        
        # Display summary statistics for numerical columns
        st.write("Summary statistics for numerical columns:")
        st.write(df.describe())
        
        # Display the first few rows of the dataset
        st.write("First few rows of the dataset:")
        st.write(df.head())

if __name__ == "__main__":
    main()
