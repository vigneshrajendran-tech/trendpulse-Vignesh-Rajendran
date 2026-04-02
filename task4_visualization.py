# 📊 Task 4 — Visualizing the analysed data

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Step 1: Setup
# -------------------------------

# Load the analysed CSV file from Task 3
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

print("Data loaded for visualization:", df.shape)

# Create output folder if not present
os.makedirs("outputs", exist_ok=True)


# -------------------------------
# Chart 1: Top 10 Stories by Score
# -------------------------------

# Sorting data to get top 10 highest scoring stories
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles for better readability
top10["short_title"] = top10["title"].str[:60]

plt.figure()

plt.barh(top10["short_title"], top10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()  # highest score on top

# Save before showing
plt.savefig("outputs/chart1_top_stories.png")

plt.close()


# -------------------------------
# Chart 2: Stories per Category
# -------------------------------

category_counts = df["category"].value_counts()

plt.figure()

plt.bar(category_counts.index, category_counts.values, color=["blue", "green", "red", "orange", "purple"])

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")

plt.close()


# -------------------------------
# Chart 3: Score vs Comments
# -------------------------------

plt.figure()

# Color based on popularity
colors = df["is_popular"].map({True: "green", False: "red"})

plt.scatter(df["score"], df["num_comments"], c=colors)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")

# Add legend manually
import matplotlib.patches as mpatches
green_patch = mpatches.Patch(color='green', label='Popular')
red_patch = mpatches.Patch(color='red', label='Not Popular')
plt.legend(handles=[green_patch, red_patch])

plt.savefig("outputs/chart3_scatter.png")

plt.close()


# -------------------------------
# Bonus: Combined Dashboard
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Chart 1
axes[0, 0].barh(top10["short_title"], top10["score"])
axes[0, 0].set_title("Top 10 Stories")
axes[0, 0].invert_yaxis()

# Chart 2
axes[0, 1].bar(category_counts.index, category_counts.values)
axes[0, 1].set_title("Stories per Category")

# Chart 3
axes[1, 0].scatter(df["score"], df["num_comments"], c=colors)
axes[1, 0].set_title("Score vs Comments")

# Empty subplot (just for layout)
axes[1, 1].axis("off")

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")

plt.close()

print("\nAll charts saved inside 'outputs/' folder")

