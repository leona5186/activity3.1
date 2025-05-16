import pandas as pd
import os


os.makedirs("data", exist_ok=True)


try:
    df = pd.read_csv("data/raw_dataset.csv")
except FileNotFoundError:
    print("❌ Error: data/raw_dataset.csv not found.")
    exit(1)


df_cleaned = df.drop_duplicates()


df_cleaned.to_csv("data/processed_dataset.csv", index=False)
df_cleaned.to_csv("processed_dataset.csv", index=False)

print("✅ Duplicates removed successfully.")
print("📝 Cleaned data saved as:")
print("   - data/processed_dataset.csv")
print("   - processed_dataset.csv (for GitHub display)")

