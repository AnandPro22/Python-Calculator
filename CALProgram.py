'''
Python program to perform addition, multiplication, substraction, division
'''

operator = input("Enter the operation: ")

def addition(*num):
    sum=0
    for i in num:
        sum += i
    return sum

def multiplication(*num):
    multiply=0
    for i in num:
        multiply *= i 
    return multiply

def substraction(*num):
    substract=0
    for i in num:
        substract = i-substract
    return substract

def division(*num):
    divide=1
    for i in num:
        divide = i/divide 
    return divide

if operator == "*" :
    x=multiplication(100,10)
    print(f"Multiplication Answear: {x}")
if operator == "+":
    y=addition(100,10)
    print(f"Addition Answear: {y}")
if operator == "-":
    z=substraction(100,10)
    print(f"Substraction Answear: {z}")
if operator == "/" :
    a=division(100,10)
    print(f"Division Answear: {a}")