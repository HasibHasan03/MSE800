import numpy as np

# Weekly temperature data in Celsius
celsius_temps = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Calculate and print the average temperature
average_temp = np.mean(celsius_temps)
print(f"Average temperature for the week: {average_temp:.2f}°C")

# 2. Determine and display the highest and lowest recorded temperatures
max_temp = np.max(celsius_temps)
min_temp = np.min(celsius_temps)
print(f"Highest temperature: {max_temp}°C")
print(f"Lowest temperature: {min_temp}°C")

# 3. Convert all temperatures to Fahrenheit and print
fahrenheit_temps = celsius_temps * 9/5 + 32
print("Temperatures in Fahrenheit:")
print(fahrenheit_temps)