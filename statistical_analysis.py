# ============================================
# STATISTICAL ANALYSIS - SPOTIFY DATASET
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Loaded Successfully!")

# ============================================
# 1. BASIC STATISTICS
# ============================================

print("\n" + "="*60)
print("BASIC STATISTICS")
print("="*60)

print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())

print("\nNumerical Summary:\n")
print(df.describe())

# ============================================
# 2. CORRELATION ANALYSIS
# ============================================

print("\n" + "="*60)
print("CORRELATION ANALYSIS")
print("="*60)

numeric_df = df.select_dtypes(include=['int64','float64'])

correlation = numeric_df.corr()

print("\nCorrelation with Popularity:\n")
print(correlation["popularity"].sort_values(ascending=False))


# 🔥 HEATMAP (UPGRADED)
plt.figure(figsize=(10,8))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    center=0,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Heatmap of Features", fontsize=14, weight='bold')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================
# 3. NORMALITY TEST (Shapiro)
# ============================================

print("\n" + "="*60)
print("NORMALITY TEST (Shapiro Test)")
print("="*60)

sample = df["popularity"].sample(5000)

stat, p_value = stats.shapiro(sample)

print("Shapiro Statistic:", stat)
print("p-value:", p_value)

if p_value > 0.05:
    print("Data is normally distributed")
else:
    print("Data is NOT normally distributed")


# ============================================
# 4. HYPOTHESIS TEST (T-Test)
# ============================================

print("\n" + "="*60)
print("HYPOTHESIS TEST: Explicit vs Non-Explicit")
print("="*60)

explicit = df[df["explicit"] == True]["popularity"]
non_explicit = df[df["explicit"] == False]["popularity"]

t_stat, p_val = stats.ttest_ind(explicit, non_explicit)

print("T-test Statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print("Significant difference between groups")
else:
    print("No significant difference between groups")


# ============================================
# 5. ANOVA TEST (Genre Impact)
# ============================================

print("\n" + "="*60)
print("ANOVA TEST: Genre vs Popularity")
print("="*60)

top_genres = df["track_genre"].value_counts().head(5).index

groups = [df[df["track_genre"] == genre]["popularity"] for genre in top_genres]

f_stat, p_val = stats.f_oneway(*groups)

print("F-statistic:", f_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print("Genres significantly affect popularity")
else:
    print("No significant effect of genre")


# ============================================
# 6. POPULARITY DISTRIBUTION (UPGRADED)
# ============================================

mean_val = df["popularity"].mean()

plt.figure(figsize=(10,6))

sns.histplot(
    df["popularity"],
    bins=30,
    kde=True,
    color="skyblue",
    edgecolor="black"
)

plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean = {mean_val:.2f}')

plt.legend()
plt.title("Popularity Distribution with Mean Indicator", fontsize=14, weight='bold')
plt.xlabel("Popularity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# ============================================
# END
# ============================================

print("\nStatistical Analysis Completed Successfully!")