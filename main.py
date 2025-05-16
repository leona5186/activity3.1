import pandas as pd

# Load dataset
df = pd.read_csv('data/raw_dataset.csv')

# Drop duplicates
df_clean = df.drop_duplicates()

# Save to data folder
df_clean.to_csv('data/processed_dataset.csv', index=False)

# ALSO save a copy to project root so it appears in GitHub
df_clean.to_csv('processed_dataset.csv', index=False)

print("Duplicates removed and saved to both data/ and root directory.")



# This is a trigger for GitHub Actions
# trigger CI/CD workflow

