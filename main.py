import pandas as pd

# Load dataset
df = pd.read_csv('data/raw_dataset.csv')

# Drop duplicates
df_clean = df.drop_duplicates()

# Save cleaned dataset
df_clean.to_csv('data/processed_dataset.csv', index=False)

print("Duplicates removed successfully.")

#trigger CI/CD workflow

