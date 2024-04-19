import operators as ops
import functions as func

# declare variables and initialise
accumulator = 0
number = 0
calc_init = True
calc_finished = False

# calculations are in string format as we will use eval() function to evaluation string into an operation
calculations = {
    "+": f"ops.add(accumulator, number)",
    "-": f"ops.subtract(accumulator, number)",
    "*": f"ops.multiply(accumulator, number)",
    "//": f"ops.divide(accumulator, number)",
}

arithmetic = []

# as long as the quit command has not been entered keep looping
while not calc_finished:
    # check to see if it's meant to be the first calculation, if so ask for the first number
    # and print the operators
    if calc_init:
        accumulator = float(input("What is the first number? "))
        print("+\n-\n*\n/")

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

    # evaluate the new value of the accumulator using the eval function to interpret the respective string
    # in the calculations list
    accumulator = eval(calculations[operator])

    #print out the final version of the equation
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
