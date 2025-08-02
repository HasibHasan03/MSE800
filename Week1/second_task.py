def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):  # Start from 2, go up to n, step by 2
        total += i
    return total

# Example usage
n = int(input("Enter a positive number: "))
if n < 1:
    print("Please enter a number greater than 0.")
elif n % 2 != 0:
    print("Please enter an odd number.")
else:
    result = sum_of_even_numbers(n)
    print(f"Sum of all even numbers from 1 to {n} is: {result}")