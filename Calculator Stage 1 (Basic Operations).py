# TODO: Write the functions for arithmetic operations here
# These functions should cover Task 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function should cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if (choice == '#'):
        return -1
    elif (choice == '$'):
        return 0  # Reset
    elif (choice in ('+', '-', '*', '/', '^', '%')):
        while True:
            num1 = str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                x1 =float(num1)
                break
            except:
                print("Not a valid number, pleae enter again")
                continue
        while True:
            num2 = str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                x2 =float(num2)
                break
            except:
                print("Not a valid number, pleae enter again")
                continue

        if choice == '+':
            print(x1, "+",x2, "=", add(x1,x2))
        elif choice == '-':
            print(x1, "-",x2, "=", subtract(x1,x2))
        elif choice == '*':
            print(x1, "*",x2, "=", multiply(x1,x2))
        elif choice == '/':
            print(x1, "/",x2, "=", divide(x1,x2))
        elif choice == '^':
            print(x1, "^",x2, "=", power(x1,x2))
        elif choice == '%':
            print(x1, "%",x2, "=", remainder(x1,x2))
        else:
            print("Something went wrong")

    else:
        print("Unrecognized operation")


# End the select_op(choice) function here
# -------------------------------------

# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    
    if (select_op(choice) == -1):
        # Terminate the program
        print("Done. Terminating")
        exit()