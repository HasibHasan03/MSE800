import numpy as np

# Define temperature and day arrays
celsius_temps = np.array([18.5, 19, 20, 25.0, 22, 30, 13.9]) 
day_array = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# 1. average temperature
average_temp = np.mean(celsius_temps)
print(f"Average temperature for the week: {average_temp:.2f}°C")

# 2. highest and lowest recorded temperatures
max_temp = np.max(celsius_temps)
min_temp = np.min(celsius_temps)
print(f"Highest temperature: {max_temp}°C")
print(f"Lowest temperature: {min_temp}°C")

# 3. Convert to Fahrenheit
fahrenheit_temps = celsius_temps * 9/5 + 32
print("Temperatures in Fahrenheit:")
print(fahrenheit_temps)

# 4. Days where temperature > 20°C
indices = np.where(celsius_temps > 20)[0]
print("Days with temperature > 20°C:")
for i in indices:
    print(f"{day_array[i]}: {celsius_temps[i]}°C")