import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, csv_file, parquet_file):
        self.csv_file = csv_file
        self.parquet_file = parquet_file
        self.data = None
        self.numeric_columns = None

    def load_data(self):
        """Load CSV into a DataFrame"""
        print("Loading CSV file...")
        self.data = pd.read_csv(self.csv_file)

        # Keep only numeric columns
        self.numeric_columns = self.data.select_dtypes(include=[np.number]).columns
        print(f"Numeric columns: {list(self.numeric_columns)}")

    def convert_to_parquet(self):
        """Save dataset as Parquet file"""
        if self.data is None:
            print("Error: Data not loaded yet!")
            return
        self.data.to_parquet(self.parquet_file, index=False)
        print(f"Data saved to Parquet: {self.parquet_file}")

    def calculate_statistics(self):
        """Compute stats for each numeric column"""
        if self.data is None:
            print("Error: Data not loaded yet!")
            return

        print("\nColumn Statistics:")
        for col in self.numeric_columns:
            series = self.data[col]

            print(f"\nColumn: {col}")
            print(f"  Max  : {series.max()}")
            print(f"  Min  : {series.min()}")
            print(f"  Mean : {series.mean()}")
            print(f"  First 5 absolute values: {series.abs().head(5).tolist()}")

def main():
    # File paths (change according to your dataset)
    csv_path = "Week3/task3/online_retail.csv"
    parquet_path = "Week3/task3/online_retail.parquet"

    # Create processor object
    processor = DataProcessor(csv_path, parquet_path)

    # Step 1: Load
    processor.load_data()

    # Step 2: Convert
    processor.convert_to_parquet()

    # Step 3: Stats
    processor.calculate_statistics()

if __name__ == "__main__":
    main()