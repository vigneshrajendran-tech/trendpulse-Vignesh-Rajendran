
import requests
import json
import time
from datetime import datetime
import os

# Config
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {
    "User-Agent": "TrendPulse/1.0"
}

# Categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}
# Helper Function
def assign_category(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title_lower:
                return category
    return "other"


# Step 1 — Get Top Story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]  # First 500
except Exception as e:
    print("Error fetching story IDs:", e)
    exit()

# Step 2 — Fetch Story Details

collected_data = {cat: [] for cat in categories.keys()}

for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()

        if story is None or "title" not in story:
            continue

        category = assign_category(story["title"])

        if category in collected_data and len(collected_data[category]) < 25:
            collected_data[category].append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by", "unknown"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        # Stop if all categories filled
        if all(len(v) >= 25 for v in collected_data.values()):
            break

    except Exception as e:
        print(f"Error fetching story {story_id}: {e}")
        continue


# Step 3 — Combine Data
final_data = []
for cat_list in collected_data.values():
    final_data.extend(cat_list)


# Step 4 — Save JSON
os.makedirs("data", exist_ok=True)

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(final_data, f, indent=4)

print(f"\n✅ Collected {len(final_data)} stories. Saved to {filename}")