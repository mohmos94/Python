# create a python calculator 

# function for addition takes two input parameter
# return the value
def addition(firste_value, second_value):
    value = firste_value + second_value
    calculator(value)
    return value


# function for subtraction takes two input parameter
# return the value
def subtraction(firste_value, second_value):
    value = firste_value - second_value
    calculator(value)
    return value


# function for multiply takes two input parameter
# return the value
def multiply(firste_value, second_value):
    value = firste_value * second_value
    calculator(value)
    return value


# function for divide takes two input parameter
# return the value
def divide(firste_value, second_value):
    value = firste_value / second_value
    calculator(value)
    return value


# function for modulo takes two input parameter
# return the value
def modulo(firste_value, second_value):
    value = firste_value % second_value
    calculator(value)
    return value

# print the calculation for the operation
def calculator(value):
    print("The answer is: {} ".format(value))

# input function takes the input from the user
# check for other operator and calls correct operator function
def input_value():
    firste_value = float(input("Enter firste value: "))
    second_value = float(input("Enter second value: "))
    operator = input("enter the operator: ")
    formating = "firste value: {}  operator: {} second value: {}"

    if operator == "+":
        print(formating.format(firste_value, operator, second_value))
        addition(firste_value, second_value)

    elif operator == "-":
        print(formating.format(firste_value, operator, second_value))
        subtraction(firste_value, second_value)

    elif operator == "*":
        print(formating.format(firste_value, operator, second_value))
        multiply(firste_value, second_value)
    elif operator == "/":
        print(formating.format(firste_value, operator, second_value))
        divide(firste_value, second_value)
    elif operator == "%":
        print(formating.format(firste_value, operator, second_value))
        modulo(firste_value, second_value)
    else:
        print("{} is not an operator".format(operator))

input_value()
