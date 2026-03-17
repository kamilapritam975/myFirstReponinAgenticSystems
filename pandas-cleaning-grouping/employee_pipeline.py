import pandas as pd
import numpy as np

# 🔹 Step 1: Create DataFrame
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("🔹 Original DataFrame:\n")
print(df)


# 🔹 Step 2: Detect Missing Values
print("\n🔹 Missing Values:\n")
print(df.isnull())


# 🔹 Step 3: Fill Missing Salary with Mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\n🔹 After Filling Missing Salary:\n")
print(df)


# 🔹 Step 4: Drop Temporary_Notes Column
df.drop("Temporary_Notes", axis=1, inplace=True)

print("\n🔹 After Dropping Temporary_Notes:\n")
print(df)


# 🔹 Step 5: Rename Salary to Annual_Salary
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\n🔹 After Renaming Column:\n")
print(df)


# 🔹 Step 6: Group By Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n🔹 Final Summary Table:\n")
print(summary)