import pandas as pd

# Load dataset
df = pd.read_csv('data/raw_dataset.csv')

# Drop duplicates
df_clean = df.drop_duplicates()

# Save cleaned dataset
df_clean.to_csv('data/processed_dataset.csv', index=False)

print("Duplicates removed successfully.")


import shutil

# Load and clean
df = pd.read_csv('data/raw_dataset.csv')
df_clean = df.drop_duplicates()
df_clean.to_csv('data/processed_dataset.csv', index=False)

# Optional: Copy it outside data folder to make it visible in root directory (GitHub shows it easier)
shutil.copy('data/processed_dataset.csv', 'processed_dataset.csv')

print("Dataset cleaned and copied successfully.")


# This is a trigger for GitHub Actions
# trigger CI/CD workflow

