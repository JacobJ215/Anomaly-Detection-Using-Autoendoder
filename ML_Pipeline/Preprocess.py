import pandas as pd

# Function to clean data: Convert to numberical values and impute missing values
def clean_data(data):
    data = data.fillna(data.mean())
    data = data.drop("Timestamp", axis=1)
    return data

# Function to normalize data betweeen 0 and 1
def normalize_data(data, is_train, output_dir='../output'):
    min_val = data.min()
    max_val = data.max()

    if is_train:
        min_val.to_pickel(f"{output_dir}/min_val.pkl")
        max_val.to_pickel(f"{output_dir}/max_val.pkl")
    else:
        min_val = pd.read_pickle(f"{output_dir}/min_val.pkl")
        max_val = pd.read_pickle(f"{output_dir}/max_val.pkl")
    
    normalized_df = (data - min_val) / (max_val - min_val)
    return normalized_df

# Function to call dependent preprocessing functions
def preprocess(data, is_train):
    print("Preprocessing has begun...")

    data = clean_data(data)
    print("Data cleaning has completed...")

    data = normalize_data(data, is_train)
    print("Data normalization has completed...")

    data = data.loc[:, ~data.columns.duplicated()]
    print("Preprocesing is complete...")
    return data
