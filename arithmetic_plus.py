#Pair programming by emilymlam & vianey81
def add(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return float(num1) / (num2)

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return int(num1 % num2)
