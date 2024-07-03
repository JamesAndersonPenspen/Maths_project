def addition():
    final_number = 0
    continue_calc = True
    while continue_calc:
        if_number = False
        while not if_number :
            initial_number = input("Enter a number you would like add: ")
            if initial_number.isdigit():
                initial_number = int(initial_number)
                if_number = True
            else:
                print("This needs to be an integer! (E.g. 10)")
        final_number += initial_number
        print("your current total is: ",final_number)
        choice_certainty = False
        while not choice_certainty:
            choice_continue = input("Would you like to contuinue adding? (yes or no) ")
            if choice_continue.lower() == "yes":
                choice_certainty = True
            elif choice_continue.lower() == "no":
                continue_calc = False
                choice_certainty = True
            else:
                print("Not a valid input please choose yes or no")



    