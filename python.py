#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).Perform the operation based on the user's input and print the result.
def calculator():
    num1 = float(input("Enter the first Number: "))
    num2 = float(input("Enter the second Number: "))
    operation = input("Enter the operation (+, -, * or /): ")
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
            
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error; divison by zero is not allowed!")

    else:
        print("Error: Input the correct details!")

calculator()