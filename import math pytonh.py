import math 


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Делить на ноль нельзя."
    else:
        return a / b


def exponentiation(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Квадратный корень из отрицательного числа нельзя найти."
    else:
        return math.sqrt(a)


def factorial(n):
 if (n <= 1):
  return 1
 else:
   return (n * factorial(n-1))


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)

def check_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print(" введите число")

def check_symbol_input(prompt):
    while True:
        symbol = input(prompt)
        if len(symbol) == 1:
            return symbol
        else:
            print(" введите только один символ.")


def check_operation_input(prompt):
    operations = ["+", "-", "*", "/", "^", "sqrt", "!", "sin", "cos", "tan"]
    while True:
        operation = input(prompt)
        if operation in operations:
            return operation
        else:
            print(" указанной вами операции нет")


def calculator():
    print("Инженерный калькулятор")
    a = check_number_input("Введите  число , с которым хотите совершать действия ")
    operation = check_operation_input("Введите операцию (+, -, *, /, ^, sqrt, !, sin, cos, tan): ")

    if operation in ["sqrt", "!", "sin", "cos", "tan"]:
        if operation == "sqrt":
            result = square_root(a)
        elif operation == "!":
            result = factorial(a)
        elif operation == "sin":
            result = sine(a)
        elif operation == "cos":
            result = cosine(a)
        elif operation == "tan":
            result = tangent(a)
            
        print(f"Результат: {result}")
    else:
        b = check_number_input("Введите второе число: ")

        if operation == "+":
            result = addition(a, b)
        elif operation == "-":
            result = subtraction(a, b)
        elif operation == "*":
            result = multiplication(a, b)
        elif operation == "/":
            result = division(a, b)
        elif operation == "^":
            result = exponentiation(a, b)

        print(f"Результат: {result}")


calculator()



