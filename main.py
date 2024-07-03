keep_going = True
count = 0
full_number = 1
while keep_going:
    count += 1
    if_number = False
    while if_number == False:
        newnumber = input("Enter a number you would like to multiply: ")
        if newnumber.isdigit():
            newnumber = int(newnumber)
            if_number = True
        else:
            print("This needs to be an integer! (E.g. 10)")
    full_number *= newnumber
    if count == 0:
        pass
    else:
        while  True:
            print("Your current total is: ",full_number,"\n Would you like to multiply it by another number? (Yes or no)")
            confirm = input()
            if confirm.lower() == "yes":
                break
            elif confirm.lower() == "no":
                keep_going = False
                break
            else: 
                print("Incorrect input - the only accepted inputs are yes and no!")