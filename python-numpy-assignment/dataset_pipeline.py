import numpy as np

# 1. Set random seed
np.random.seed(42)

# 2. Generate dataset (100 samples, 3 features)
data = np.random.rand(100, 3)

# 3. Compute mean and standard deviation per feature
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

# 4. Normalize dataset using broadcasting
normalized = (data - mean) / std

# 5. Split dataset (80% train, 20% test)
split_index = int(0.8 * normalized.shape[0])

train_data = normalized[:split_index]
test_data = normalized[split_index:]

# 6. Modify sliced value to demonstrate view behavior
train_data[0, 0] = 999

# 7. Print results
print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Standard deviation shape:", std.shape)

print("Training data shape:", train_data.shape)
print("Test data shape:", test_data.shape)

print("Note: Modifying the slice affected the original array (NumPy slicing returns a view).")