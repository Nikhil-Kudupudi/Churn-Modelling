# Install dependencies as needed:
# pip install kagglehub[polars-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "Churn_Modelling.csv"

# Load the latest version
lf = kagglehub.load_dataset(
  KaggleDatasetAdapter.POLARS,
  "kartiksaini18/churn-bank-customer",
  file_path,
  # Provide any additional arguments like
  # sql_query, polars_frame_type, or 
  # polars_kwargs.
  # See the documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpolars
)

def get_churn_data():
    """
    Load the churn data from the dataset.
    
    Returns:
        pl.DataFrame: The churn data as a Polars DataFrame.
    """
    try:
    # Load the data using the loaded file
        df = lf.collect()
        df.write_csv("data/raw/Churn_Modelling.csv")  # Save to local file if needed
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    churn_data = get_churn_data()
    if churn_data is not None:
        print("Churn data loaded successfully.")
        print(churn_data.head())
    else:
        print("Failed to load churn data.")