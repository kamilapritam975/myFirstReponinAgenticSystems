import pandas as pd

print("=== AI Dataset Inspection Pipeline ===\n")

# Step 1: Create sample dataset
data = {
    "Name": ["Rahul", "Pritam", "Aman", "Neha", "Riya", "Karan", "Anita", "Vikram"],
    "Age": [22, 18, 25, 21, 19, 24, 23, 20],
    "Score": [85, 92, 78, 88, 95, 67, 81, 73],
    "Label": ["Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Fail"]
}

df = pd.DataFrame(data)

# Step 2: Save dataset to CSV
df.to_csv("sample_dataset.csv", index=False)

print("Dataset created and saved as sample_dataset.csv\n")

# Step 3: Load dataset
dataset = pd.read_csv("sample_dataset.csv")

# Step 4: Show first 5 rows
print("First 5 rows:")
print(dataset.head())
print("\n")

# Step 5: Show last 5 rows
print("Last 5 rows:")
print(dataset.tail())
print("\n")

# Step 6: Dataset info
print("Dataset Info:")
print(dataset.info())
print("\n")

# Step 7: Summary statistics
print("Summary Statistics:")
print(dataset.describe())
print("\n")

# Step 8: Select single column
age_column = dataset["Age"]
print("Single Column Selected (Age):")
print(age_column)
print("\n")

# Step 9: Select multiple columns
selected_columns = dataset[["Name", "Score"]]
print("Multiple Columns Selected (Name, Score):")
print(selected_columns)
print("\n")

# Step 10: Filter rows
filtered_rows = dataset[dataset["Score"] > 80]

print("Filtered Rows (Score > 80):")
print(filtered_rows)