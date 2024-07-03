from multiply import multiply
from division import divide
from subtract import subtract
from addition import addition

keep_going = True
while keep_going:
    choice = input("What would you like to do? (add, subtract,multiply or divide) ")
    if choice.lower() == "add":
        addition()
    elif choice.lower() == "subtract":
        subtract()
    elif choice.lower() == "multiply":
        multiply()
    elif choice.lower() == "divide":
        divide()
    else:
        print("This is not a valid option, valid options are listed above.")
    input_valid = False
    while not input_valid:
        keep_going_choice = input("Would you like to do another calculation? (yes or no) ")
        if keep_going_choice.lower() == "yes":
            input_valid = True
        elif keep_going_choice.lower() == "no":
            input_valid = True 
            keep_going = False
        else:
            print("This is not a valid input, valid inputs are yes or no.")



