import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import get_data

# Title
st.title("📊 Simple Data Dashboard")

# Load Data
df = get_data()

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# Analysis
# -----------------------------

# Posts per user
posts_per_user = df.groupby("user_id").size()

# -----------------------------
# Visualization 1: Bar Chart
# -----------------------------
st.subheader("Posts per User")

fig1, ax1 = plt.subplots()
ax1.bar(posts_per_user.index, posts_per_user.values)
ax1.set_xlabel("User ID")
ax1.set_ylabel("Number of Posts")

st.pyplot(fig1)

# -----------------------------
# Visualization 2: Histogram
# -----------------------------
st.subheader("Post Length Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(df["post_length"])
ax2.set_xlabel("Post Length")
ax2.set_ylabel("Frequency")

st.pyplot(fig2)