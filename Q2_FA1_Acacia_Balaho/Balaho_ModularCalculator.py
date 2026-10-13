# Introduce the user to the program.
print("This is a modular calculator program.")

# Ask the user to input 2 numbers that he/she wants to be calculated. Validate the user's input (responds with a message if the input for this is invalid).
while True:
    try:
        num1 = float(input("Please enter your 1st number: "))
        num2 = float(input("Please enter your 2nd number: "))
        break

    except ValueError:
        print("Invalid input! Please enter numbers only. Try again.")

# Show the user the mathematical operations that can be chosen and used to calculate the user's 2 numbers. Label for future input.
print("Addition = 1")
print("Subtraction = 2")
print("Multiplication = 3")
print("Division = 4")

# Ask the user for the operation that he/she wants to calculate the user's 2 numbers with. Also validate the user's input (also responds with a message if the input for this is invalid).
while True:
    try:
        operation = int(input(
            "Please enter the number corresponding to the mathematical operation you want to use on your numbers: "
        ))

        if operation in (1, 2, 3, 4):
            break
        else:
            print("Invalid input! Please enter the number corresponding to your mathematical operation of your choice displayed.")

    except ValueError:
        print("Invalid input! Enter the number corresponding to your choice only.")

# Behind the scenes processes in calculating the result based on all inputs of the user. Also validates stuff like dividing by 0 and overall inputs. Displays result at the end.
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

if operation == 1:
    print("The result based on your inputs is", addition(num1, num2))

elif operation == 2:
    print("The result based on your inputs is", subtraction(num1, num2))

elif operation == 3:
    print("The result based on your inputs is", multiplication(num1, num2))

elif operation == 4:
    if num2 != 0:
        print("The result based on your inputs is", division(num1, num2))
    else:
        print("Error: division by 0 is undefined.")

else:
  print("Invalid input/s. Please try again.")

# Reflection: I created four functions for addition, subtraction, multiplication, and division, using num1 and num2 as parameters. The arguments passed when calling these functions are the two numbers entered by the user. Each function returns a calculated value, which is displayed using print(). Modular programming makes the code more organized, readable, and easier to maintain.
