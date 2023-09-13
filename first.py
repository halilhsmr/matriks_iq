import math

number = int(input("enter a num: "))

fact = 1
i = 1

while i <= number:
    fact *= i
    i += 1
print(fact)

print("factorial is: ", math.factorial(number))
