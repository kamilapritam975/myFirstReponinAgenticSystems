import numpy as np

# Step 1: Create NumPy array
data = np.array([10, 20, 30, 40])

# Step 2: Calculate mean
mean = np.mean(data)

# Step 3: Calculate standard deviation
std = np.std(data)

# Step 4: Normalize data
normalized = (data - mean) / std

# Step 5: Reshape into 2D
reshaped = normalized.reshape(2, 2)

# Step 6: Print results
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized data:", normalized)
print("Reshaped data:")
print(reshaped)
print("Reshaped data shape:", reshaped.shape)