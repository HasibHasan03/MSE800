# print("Hello Emam!")

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(n, 0, -1):  # From n down to 1
        result = result * i
    return result

# Example
num = int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}")