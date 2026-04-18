# ============================================
# FINAL EDA - ADVANCED VISUALS (UPDATED)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

df = pd.read_csv("cleaned_dataset.csv")

# Convert duration
df["duration_min"] = df["duration_ms"] / 60000

# ============================================
# OBJECTIVE 1: HIGH POPULARITY GENRES
# ============================================

top_songs = df[df["popularity"] > 70]

plt.figure()
sns.countplot(
    y="track_genre",
    data=top_songs,
    order=top_songs["track_genre"].value_counts().head(10).index,
    hue="track_genre",
    palette="viridis",
    legend=False
)
plt.title("Genres Dominating High Popularity Songs")
plt.xlabel("Number of Highly Popular Songs")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()


# ============================================
# OBJECTIVE 2: DANCEABILITY DISTRIBUTION
# ============================================

top_genres = df["track_genre"].value_counts().head(6).index

plt.figure()
sns.boxplot(
    x="track_genre",
    y="danceability",
    data=df[df["track_genre"].isin(top_genres)],
    hue="track_genre",
    palette="Set2",
    legend=False
)
plt.title("Danceability Distribution Across Major Genres")
plt.xlabel("Genre")
plt.ylabel("Danceability")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================
# OBJECTIVE 3: ENERGY VS POPULARITY SUCCESS
# ============================================

bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
labels = ["0-0.2", "0.2-0.4", "0.4-0.6", "0.6-0.8", "0.8-1.0"]

df["energy_range"] = pd.cut(df["energy"], bins=bins, labels=labels)

top_songs = df[df["popularity"] > 70]

energy_success = top_songs["energy_range"].value_counts().sort_index()

plt.figure()
sns.barplot(
    x=energy_success.index,
    y=energy_success.values,
    hue=energy_success.index,
    palette="magma",
    legend=False
)
plt.title("High Popularity Songs Across Energy Levels")
plt.xlabel("Energy Range")
plt.ylabel("Number of High Popularity Songs")
plt.tight_layout()
plt.show()


# ============================================
# OBJECTIVE 4: TRACK FREQUENCY BY DURATION
# ============================================

bins = [0, 2, 4, 6, 8, 10]
labels = ["0-2", "2-4", "4-6", "6-8", "8-10"]

df["duration_range"] = pd.cut(df["duration_min"], bins=bins, labels=labels)

duration_count = df["duration_range"].value_counts().sort_index()

plt.figure()
sns.barplot(
    x=duration_count.index,
    y=duration_count.values,
    hue=duration_count.index,
    palette="crest",
    legend=False
)
plt.title("Track Frequency by Duration Range")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Tracks")
plt.tight_layout()
plt.show()


# ============================================
# OBJECTIVE 5: DURATION VS POPULARITY
# ============================================

duration_pop = df.groupby("duration_range")["popularity"].mean()

plt.figure()
sns.lineplot(
    x=duration_pop.index,
    y=duration_pop.values,
    marker="o",
    color="purple"
)
plt.title("Average Popularity by Duration Range")
plt.xlabel("Duration Range")
plt.ylabel("Popularity")
plt.tight_layout()
plt.show()


# ============================================
# OBJECTIVE 6: POPULARITY DISTRIBUTION
# ============================================

plt.figure()            
sns.kdeplot(
    df["popularity"],
    fill=True,
    color="teal"
)
plt.title("Popularity Density Distribution")
plt.xlabel("Popularity")
plt.ylabel("Density")
plt.tight_layout()
plt.show()


# ============================================
# END
# ============================================

print("\nEDA Completed Successfully!")