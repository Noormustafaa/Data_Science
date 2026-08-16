
# Section 1: What is NumPy and Why is it Essential?
# NumPy stands for Numerical Python. It is the most fundamental library in Python used for mathematical and scientific calculations.
# Python Lists vs NumPy Arrays
# You might ask, "We already have Python Lists to store data, so why do we need NumPy?" There are 3 major reasons:
# 1. Speed: NumPy arrays are 10x to 100x faster than standard Python lists because they are written in C.
# 2. Memory: They occupy much less memory space because, unlike lists, they don't store separate memory addresses for each element.
# 3. Element-wise Operations: You cannot perform direct math on lists (e.g., [1, 2] + 2 will throw an error), whereas in NumPy, it works effortlessly.

# Section 2: Basic Concepts (Creation & Inspection)
# First of all, you need to install and import NumPy:
# pip install numpy

# Note:
# python -m pip install --upgrade pip
import numpy as np

print("Noor")

# 1-Dimensional Array (Vector)
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

print("Array Type:", type(arr))
print(arr)

# 2-Dimensional Array (Matrix - Rows and Columns)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2d)

# 2. Checking Array Details (Attributes)
# When you have an array, these tools are used to check its properties:

print("Shape (Rows, Columns):", arr2d.shape)  # Output: (2, 3)
print("Dimensions (Number of Dimensions):", arr2d.ndim)  # Output: 2
print("Data Type:", arr2d.dtype)  # Output: int64 (or int32)
print("Total Elements:", arr2d.size)  # Output: 6

