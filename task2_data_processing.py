# 📊 Task 2 — Cleaning the JSON data and saving as CSV

import pandas as pd

# -------------------------------
# Step 1: Load the JSON file
# -------------------------------

# I am loading the JSON file generated from Task 1
file_path = "data/trends_20260402.json"   # update date if needed

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from the JSON file")

# -------------------------------
# Step 2: Cleaning the data
# -------------------------------

# 1. Remove duplicate rows (sometimes same story may appear twice)
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))

# 2. Remove rows with missing important values
# We need post_id, title, and score for analysis
df = df.dropna(subset=["post_id", "title", "score"])
print("Rows after removing missing values:", len(df))

# 3. Fix data types (ensure numbers are stored correctly)
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# 4. Remove low-quality posts
# Here I am filtering out stories with very low score (<=5)
df = df[df["score"] > 5]
print("Rows after removing low-score posts:", len(df))

# 5. Clean text data
# Removing extra spaces from titles
df["title"] = df["title"].str.strip()

# -------------------------------
# Step 3: Save cleaned data
# -------------------------------

output_path = "data/trends_clean.csv"

# Saving the cleaned dataframe into CSV format
df.to_csv(output_path, index=False)

print(f"\nCleaned data saved to: {output_path}")
print(f"Total rows saved: {len(df)}")

# -------------------------------
# Step 4: Quick Summary
# -------------------------------

# Display how many stories belong to each category
print("\nStories count per category:")
print(df["category"].value_counts())