# ===========================================
# PYTHON PACKAGES: NumPy, Pandas, Matplotlib, Scikit-Learn
# ===========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- NumPy ----------
arr = np.array([10, 20, 30, 40])
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))
print()

# ---------- Pandas ----------
data = {
    "Name": ["Amit", "Riya", "Karan", "Sara"],
    "Age": [25, 28, 22, 24],
    "Marks": [85, 90, 78, 92]
}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df, "\n")

# ---------- Matplotlib ----------
plt.bar(df["Name"], df["Marks"], color='skyblue')
plt.title("Student Marks Visualization")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()
