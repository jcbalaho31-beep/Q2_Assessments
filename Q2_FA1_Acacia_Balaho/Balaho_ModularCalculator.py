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
def addition():
    return num1 + num2

def subtraction():
    return num1 - num2

def multiplication():
    return num1 * num2

def division():
    return num1 / num2

if operation == 1:
    print("The result based on your inputs is", addition())

elif operation == 2:
    print("The result based on your inputs is", subtraction())

elif operation == 3:
    print("The result based on your inputs is", multiplication())

elif operation == 4:
    if num2 != 0:
        print("The result based on your inputs is", division())
    else:
        print("Error: division by 0 is undefined.")

else:
  print("Invalid input/s. Please try again.")

# Reflection: Learning and doing modular programming was so fun. Creating the functions took some time along with the parameters used. I had an issue with creating the functions because I still did not know how to use the return statement/keyword, which made the code always give a result of "None." It was something new I learned. Another thing that took some time is making the validations such as letting the user know division with 0 is undefined and making sure the inputs are in range.
