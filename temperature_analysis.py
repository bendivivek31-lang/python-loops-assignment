import numpy as np
import time

# Task 1: Temperature Conversion
temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
avg_fahrenheit = np.round(np.mean(temps_fahrenheit), 2)
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)
print()

# Task 2: Array Shape and Statistics
test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape:", test_scores.shape)
print("Total elements:", test_scores.size)
highest = np.max(test_scores)
lowest = np.min(test_scores)
score_range = highest - lowest
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Range:", score_range)
print()

# Task 3: NumPy vs Python List Performance
arr = np.arange(1, 50001)
lst = list(range(1, 50001))

start = time.time()
numpy_sum = np.sum(arr)
numpy_time = time.time() - start
start = time.time()
python_sum = sum(lst)
python_time = time.time() - start
speedup = python_time / numpy_time

print(f"NumPy sum: {numpy_sum}")
print(f"Python sum: {python_sum}")
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")
print(f"NumPy is {speedup:.1f}x faster")
