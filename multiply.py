full_number = 1
another_number = True
while another_number:
    number_good = False
    while not number_good:
        new_number = input("Please enter the number you would like to multiply by: ")
        if new_number.isdigit():
            new_number = int(new_number)
            number_good = True
        else:
            print("The number must be an integer!")
    full_number *= new_number
    print("Your full multiplication is:", full_number)
    
    accepted_input = False
    while not accepted_input:
        keep_going = input("Would you like to multiply by another number? (yes or no) ")
        if keep_going.lower() == "yes":
            accepted_input = True
        elif keep_going.lower() == "no":
            another_number = False
            accepted_input = True
        else:
            print("This is not an accepted input. Please input 'yes' or 'no'.")
