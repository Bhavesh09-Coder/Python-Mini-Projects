import numpy as np
import matplotlib.pyplot as plt

# Define the exercises
exercises = ["Push-ups", "Sit-ups", "Squats", "Running (km)", "Cycling (km)"]

# Number of days to track
days = np.array([1, 2, 3, 4, 5, 6, 7])

# Randomly generated data representing progress over a week
push_ups = np.array([20, 22, 24, 26, 28, 30, 32])
sit_ups = np.array([15, 16, 18, 20, 21, 23, 25])
squats = np.array([30, 35, 40, 42, 45, 48, 50])
running = np.array([2, 2.5, 3, 3.2, 3.5, 3.8, 4])
cycling = np.array([5, 6, 6.5, 7, 7.5, 8, 9])

# Create a figure and axis for plotting
plt.figure(figsize=(10, 6))

# Plot the data for each exercise
plt.plot(days, push_ups, label="Push-ups")
plt.plot(days, sit_ups, label="Sit-ups")
plt.plot(days, squats, label="Squats")
plt.plot(days, running, label="Running (km)")
plt.plot(days, cycling, label="Cycling (km)")

# Add titles and labels
plt.title("Fitness Progress Over a Week")
plt.xlabel("Days")
plt.ylabel("Number/Reps/Distance")
plt.legend()

# Display the graph
plt.grid(True)
plt.show()
