import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs list
epochs = list(range(1, 11))

# Step 2: Generate synthetic loss values
np.random.seed(0)  # for same result every time
loss = np.random.uniform(0.2, 1.0, size=10)

# =========================
# LINE PLOT (Loss vs Epoch)
# =========================
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue')
plt.title("Loss vs Epoch (Line Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# =========================
# SCATTER PLOT (Epoch vs Loss)
# =========================
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss, color='red')
plt.title("Epoch vs Loss (Scatter Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# =========================
# BAR CHART (Model Accuracy)
# =========================
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy, color=['green', 'blue', 'orange'])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0, 1)  # accuracy range fix
plt.grid(axis='y')
plt.show()