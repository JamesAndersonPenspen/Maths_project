keep_going = True
count = 0
full_number = 0
while keep_going:
    if_number = False
    while if_number == False:
        newnumber = input("Enter a number you would like to add: ")
        if newnumber.isdigit():
            newnumber = int(newnumber)
            if_number = True
        else:
            print("This needs to be an integer! (E.g. 10)")
    full_number += newnumber
    if count == 0:
        count += 1
        pass
    else:
        while  True:
            print("Your current total is: ",full_number,"\n Would you like to add another number? (Yes or no)")
            confirm = input()
            if confirm.lower() == "yes":
                count += 1
                break
            elif confirm.lower() == "no":
                keep_going = False
                break
            else: 
                print("Incorrect input - the only accepted inputs are yes and no!")
            count += 1