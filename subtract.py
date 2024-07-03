def subtract():
    final_number = 0
    if_number = False
    while if_number == False:
        initial_number = input("Enter a number you would like to start with: ")
        if initial_number.isdigit():
            initial_number = int(initial_number)
            if_number = True
        else:
            print("This needs to be an integer! (E.g. 10)")
    if_number2 = False
    while if_number2 == False:
        subtracted_number = input("Enter a number you would like to subtract from the first number : ")
        if subtracted_number.isdigit():
            subtracted_number = int(subtracted_number)
            if_number2 = True
        else:
            print("This needs to be an integer! (E.g. 10)")

    final_number = initial_number - subtracted_number
    print("Your final number is: ",final_number)