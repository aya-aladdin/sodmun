from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define timestamps
start_time = datetime.strptime("3/21/2025 19:47:01", "%m/%d/%Y %H:%M:%S")
end_time = datetime.strptime("6/2/2025 15:56:43", "%m/%d/%Y %H:%M:%S")

# Calculate total seconds between timestamps
total_seconds = (end_time - start_time).total_seconds()

# Create 385 evenly spaced timestamps from 0 to total_seconds
t_data = np.linspace(0, total_seconds, 385)
y_data = np.arange(1, 386)

# Exponential model: y = a * exp(b * t)
def exponential_model(t, a, b):
    return a * np.exp(b * t)

# Fit the model
params, _ = curve_fit(exponential_model, t_data, y_data, p0=(1, 1e-6))
a, b = params

# Generate predictions
fitted_y = exponential_model(t_data, a, b)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t_data / (60 * 60 * 24), y_data, 'ro', label='Original Data')  # x-axis in days
plt.plot(t_data / (60 * 60 * 24), fitted_y, 'b-', label='Exponential Fit')
plt.xlabel("Days since 3/21/2025")
plt.ylabel("Index")
plt.title("Exponential Fit: Index Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Output the equation
print(f"Exponential Model: Index(t) = {a:.2f} * exp({b:.2e} * t)")


