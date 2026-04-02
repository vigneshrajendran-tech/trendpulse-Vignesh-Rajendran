# 📊 Task 3 — Data Analysis using Pandas and NumPy

import pandas as pd
import numpy as np

# -------------------------------
# Step 1: Load the cleaned CSV
# -------------------------------

# Loading the cleaned dataset from Task 2
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape of data (rows, columns):", df.shape)

# Display first few rows to understand the data
print("\nFirst 5 rows:")
print(df.head())

# -------------------------------
# Basic averages
# -------------------------------

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))

# -------------------------------
# Step 2: NumPy Analysis
# -------------------------------

scores = df["score"].values

print("\n--- NumPy Statistics ---")

print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Standard deviation:", np.std(scores))

print("Maximum score:", np.max(scores))
print("Minimum score:", np.min(scores))

# Category with most stories
most_category = df["category"].value_counts().idxmax()
count_category = df["category"].value_counts().max()

print(f"\nCategory with most stories: {most_category} ({count_category} stories)")

# Story with highest comments
top_story = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print("Title:", top_story["title"])
print("Comments:", top_story["num_comments"])

# -------------------------------
# Step 3: Add New Columns
# -------------------------------

# Engagement = how active the discussion is compared to score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Mark stories as popular if score is above average
df["is_popular"] = df["score"] > avg_score

print("\nNew columns added: engagement, is_popular")

# -------------------------------
# Step 4: Save Final Output
# -------------------------------

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print(f"\nFinal data saved to {output_file}")