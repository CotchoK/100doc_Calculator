import operators as ops
import functions as func

# declare variables and initialise
accumulator = 0
number = 0
calc_init = True
calc_finished = False

# references to functions are stored as variables in a dictionary, which can be called later.
calculations = {
    "+": ops.add,
    "-": ops.subtract,
    "*": ops.multiply,
    "//": ops.divide,
}

arithmetic = []

# as long as the quit command has not been entered keep looping
while not calc_finished:
    # check to see if it's meant to be the first calculation, if so ask for the first number
    # and print the operators
    if calc_init:
        accumulator = float(input("What is the first number? "))
        print("+\n-\n*\n/") # we should make this dynamic based on the operations in the calculations dictionary

    # we want to wipe clean the arithmetic list to start fresh
    arithmetic.clear()

    # add the accumulator to the list
    arithmetic.append(str(accumulator))

    # ask user to choose an operation
    operator = input("Pick an operation: ")

    # add the operator to the list
    arithmetic.append(str(operator))

    # ask the user for the next number
    number = float(input("What is the next number? "))

    # add the number to the list
    arithmetic.append(str(number))

    # stringify the items in the list for print out
    arith_string = func.calc_string(arithmetic)


    # print(calculations[operator]) # test to show that it refers to a function that is at memory location x
    # This line references the function that is in the dictionary and we pass any parameters required via succeeding parentheses
    accumulator = calculations[operator](accumulator, number)

    # print out the final version of the equation
    print(arith_string + " = " + str(accumulator))

    # ask user if they want to continue with the current result
    # or if they want to start a new calc
    # or if they want to quit
    response = input(f"Type 'y' to continue calculating with {accumulator} \n"
                     f", or type 'n' to start a new calculation \n"
                     f", or type 'q' to exit \n")

    # if yes, recommence loop but with calc_init flag as false ( we want to re-use the current accumulator value)
    if response == 'y':
        calc_init = False
    # if no, recommence loop but also restart calculation with a new initial number
    elif response == 'n':
        calc_init = True
    # if q, then quit the program
    else:
        calc_finished = True
