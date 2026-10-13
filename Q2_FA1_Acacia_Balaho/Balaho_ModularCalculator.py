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
            print("Invalid input! Please choose the numbers from 1 to 4 based on the operations of choice.")

    except ValueError:
        print("Invalid input! Please input a whole number from 1 to 4.")

# Behind the scenes processes in calculating the result based on all inputs of the user. Also validates stuff like dividing by 0 and overall inputs. Displays result at the end.
if operation == 1:
    print("The result based on your inputs is", num1 + num2)

elif operation == 2:
    print("The result based on your inputs is", num1 - num2)

elif operation == 3:
    print("The result based on your inputs is", num1 * num2)

elif operation == 4:
    if num2 != 0:
        print("The result based on your inputs is", num1 / num2)
    else:
        print("Error: division by 0 is undefined.")

else:
  print("Invalid input/s. Please try again.")

# Reflection: Learning and doing modular programming was so fun. Creating the parameters used took some time because I wanted to validate the inputs for them
