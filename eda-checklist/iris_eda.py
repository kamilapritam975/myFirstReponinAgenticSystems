# Import libraries
import pandas as pd
import plotly.express as px

# Load dataset (online CSV)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# -------------------------------
# 1. Inspect Dataset Structure
# -------------------------------
print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# Observation: Dataset has 150 rows and 5 columns

# -------------------------------
# 2. Column Info + Missing Values
# -------------------------------
print("\nColumn Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Observation: No missing values found

# -------------------------------
# 3. Feature Distribution (Petal Length)
# -------------------------------
fig = px.histogram(df, x="petal_length", color="species",
                   title="Distribution of Petal Length")
fig.show()

# Observation:
# Setosa has smaller petal length
# Virginica has larger petal length

# -------------------------------
# 4. Outlier Detection (Box Plot)
# -------------------------------
fig = px.box(df, y="petal_length", color="species",
             title="Outliers in Petal Length")
fig.show()

# Observation:
# Few minor outliers in versicolor/virginica

# -------------------------------
# 5. Relationship Between Variables
# -------------------------------
fig = px.scatter(df, x="petal_length", y="petal_width",
                 color="species",
                 title="Petal Length vs Petal Width")
fig.show()

# Observation:
# Strong positive correlation between petal length & width

# -------------------------------
# 6. Correlation Analysis
# -------------------------------
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr)

fig = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
fig.show()

# Observation:
# Petal length and width highly correlated

# -------------------------------
# 7. Species Comparison
# -------------------------------
fig = px.scatter_matrix(df,
                        dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
                        color="species",
                        title="Scatter Matrix of Features")
fig.show()

# Observation:
# Setosa is clearly separable
# Versicolor & Virginica overlap slightly