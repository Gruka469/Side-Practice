n = int(input())
factorial = 1

i = 1

while i <= n:
    factorial *= i
    i += 1
    
print(f"The factorial of {n} is {factorial}")