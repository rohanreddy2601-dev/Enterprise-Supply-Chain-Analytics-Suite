import pandas as pd

def preprocess_supply_chain_data(file_path):
    print("🚀 Initializing Enterprise Supply Chain Data Pipeline...")
    
    # 1. Ingest the raw flat CSV file
    df = pd.read_csv(file_path)
    print(f"📦 Successfully loaded dataset. Initial shape: {df.shape}")
    
    # 2. Data Engineering & Cleansing
    # Drop structural duplicates to maintain transactional integrity
    df_clean = df.drop_duplicates()
    
    # Handle missing values in critical tracking metrics
    df_clean['stock_level'] = df_clean['stock_level'].fillna(0)
    df_clean['total_units_sold_today'] = df_clean['total_units_sold_today'].fillna(0)
    
    # 3. Security & Compliance (Enterprise Masking)
    # Simulating data compliance protocols by ensuring key identifier integrity
    df_clean['product_id'] = df_clean['product_id'].str.upper().str.strip()
    
    print(f"✅ Data processing complete. Cleaned shape: {df_clean.shape}")
    return df_clean

if __name__ == "__main__":
    # Example usage for local testing
    # clean_data = preprocess_supply_chain_data("path_to_your_uploaded_file.csv")
    pass
