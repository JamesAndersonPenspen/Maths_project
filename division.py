def divide():
    number_good = False
    while not number_good:
        initial_number = input("Please enter the number you would like to start with : ")
        if initial_number.isdigit():
            initial_number = int(initial_number)
            number_good = True
        else:
            print("This needs to ba an integer! E.g. 7")
    number_good2 = False
    while not number_good2:
        divider_number = input("Please enter the number you would like to divide the first by : ")
        if divider_number.isdigit():
            divider_number = int(divider_number)
            number_good2 = True
        else:
            print("This needs to ba an integer! E.g. 7")
    final_number = initial_number/divider_number 
    print("Your final number is : ",final_number)


