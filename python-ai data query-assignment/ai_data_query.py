import pandas as pd

# -----------------------------
# Create Sample Dataset
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 92, 78, 88, 67, 91],
    "Passed": [True, True, False, True, False, True],
    "Category": ["A", "A", "B", "B", "A", "A"]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:\n")
print(df)

# -----------------------------
# Select single column
# -----------------------------
print("\nOnly Names:\n")
print(df["Name"])

# -----------------------------
# Select multiple columns
# -----------------------------
print("\nName and Score DataFrame:\n")
name_score_df = df[["Name", "Score"]]
print(name_score_df)

# -----------------------------
# Use iloc (first 3 rows)
# -----------------------------
print("\nFirst 3 rows using iloc:\n")
print(df.iloc[:3])

# -----------------------------
# Use loc with meaningful index
# -----------------------------
df_indexed = df.set_index("Name")

print("\nUsing loc to access Alice:\n")
print(df_indexed.loc["Alice"])

# -----------------------------
# Filter Score > 85
# -----------------------------
print("\nStudents with Score > 85:\n")
high_score = df[df["Score"] > 85]
print(high_score)

# -----------------------------
# Filter Score > 85 AND Passed True
# -----------------------------
print("\nStudents with Score > 85 AND Passed = True:\n")
filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(filtered)

# -----------------------------
# Sort descending by Score
# -----------------------------
print("\nSorted by Score (Descending):\n")
sorted_students = filtered.sort_values(by="Score", ascending=False)
print(sorted_students)

# -----------------------------
# Chained filtering + sorting
# -----------------------------
print("\nHigh-performing students:\n")

high_performers = (
    df[(df["Score"] > 85) & (df["Passed"] == True)]
    .sort_values(by="Score", ascending=False)
)[["Name", "Score"]]

print(high_performers)