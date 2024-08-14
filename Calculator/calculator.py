print("\t\tMy Calculator")
print("\t\t=============")
first_num = input("Enter First Number...?")
second_num = input("Enter Second Number...?")
operation = input(
    """What do you want to perform:..
                  Add
                  Subtract
                  Multiply
                  Divide
                  Modulus
                  ..."""
)
if operation.lower() == "Add".lower():
    print("Addition of two numbers is: ", int(first_num) + int(second_num))
elif operation.lower() == "Subtract".lower():
    print("Subtraction of two numbers is: ", int(first_num) - int(second_num))
elif operation.lower() == "Multiply".lower():
    print("Multiplication of two numbers is: ", int(first_num) * int(second_num))
elif operation.lower() == "Divide".lower():
    if int(second_num) != 0:
        print("Division of two numbers is: ", int(first_num) / int(second_num))
    else:
        print("Error! Division by zero is not allowed")
elif operation.lower() == "Modulus".lower():
    if int(second_num) != 0:
        print("Modulus of two numbers is: ", int(first_num) % int(second_num))
    else:
        print("Error! Division by zero is not allowed")
