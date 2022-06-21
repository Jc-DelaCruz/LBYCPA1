import os

def clear():
    os.system('cls')

def pause():
    os.system("pause")

def gpa_calculator():
    print("Loading... GPA Calculator Function ---")
    # pass

def flowchartExit():
    print()
    print("Do you want to view other Flowcharts?")
    print("1 - Flowcharts Restart")
    print("2 - Main Menu")
    print("2 - Exit")
    while True:
        print()
        ch = input("Choose a Term: ")
        if ch in ['1','2','3']:
            break
    if ch == '1':
        pause()
        flowchart()
    elif ch == '2':
        pause()
        mainMenu()
    elif ch == '3':
        print("Thank you for using the program!")
        pause()

def flowchart():
    clear()
    print("=====================")
    print("Flowchart")
    print("=====================")
    print("1 - 1st Term")
    print("2 - 2nd Term")
    print("3 - 3rd Term")
    print("4 - Exit")
    while True:
        print()
        term = input("Choose a Term: ")
        if term in ['1','2','3','4']:
            break
        
    if term == '1':
        with open('term1.txt') as table1:
            term1 = table1.read()
            print("\n",term1)
        flowchartExit()


    elif term == '2':
        with open('term2.txt') as table2:
            term2 = table2.read()
            print("\n",term2)
        flowchartExit()


    elif term == '3':
        with open('term3.txt') as table3:
            term3 = table3.read()
            print("\n",term3)
        flowchartExit()

    elif term == '4':
        print("Thank you for using the Program!")
        pause()
        return 0

    else:
        print("Invalid Input... Try Again..")
        pause()
        flowchart()
    # pass

def help_desk():
    print("Loading... Help Desk Function ---")
    # pass

def mainMenu():
    clear()
    print("=====================")
    print("CpE Frosh Companion")
    print("=====================")
    print()
    print("Welcome Froshies!")
    print()
    print("1 - GPA Calculator")
    print("2 - Flowcharts")
    print("3 - Help Desk / FAQs")
    print("4 - Exit Program")
    while True:
        print()
        userCh = input("Choose an Option: ")
        if userCh in ['1', '2', '3','4']:
            break
    if userCh == '1':
        gpa_calculator()
    elif userCh == '2':
        flowchart()
    elif userCh == '3':
        help_desk()
    elif userCh == '4':
        print("Thank you for using the Program!")
        pause()
        return 0
    else:
        print("Invalid Input Try again...")
        pause()
        mainMenu()
    

def register():
    clear()
    print("-------------")
    print("REGISTRATION")
    print("-------------")
    print()

    un = input("Create Username: ")
    pw = input("Create Password: ")
    pw1 = input("Confirm your Password: ")
    acc = open("accountfile.txt","w")
    acc.write(un + " " + pw)
    acc.write("\n")
    acc.close()
    if pw != pw1:
            print("\nPasswords don't match, restart")
            pause()
            register()
    else:
        if len(pw)<=6:
            print("\nPassword too short, restart: ")
            pause()
            register()
        else:
            print("\nCongratulations! Registration Success")
            pause()
            main()

def login():
    clear()
    print("-------------")
    print("LOGIN")
    print("-------------")
    print()
    un = input("Enter Username: ")
    pw = input("Enter Password: ")
    with open ("accountfile.txt", "r") as account:
        for line in account:
            account_info = line.rstrip().split(" ")
            if un == account_info[0] and pw == account_info[1]:
                print("\nLogin Successful!")
                pause()
                mainMenu()
            else:
                print("\nInvalid Username / Password! Try again...")
                pause()
                login()

def main():
    clear()
    print("-------------------------------------------")
    print("Welcome to Frosh Companion: Login / Register")
    print("-------------------------------------------")
    print()
    print("1 - Register")
    print("2 - Login")
    print("3 - Exit")
    print()
    while True:
        print()
        userCh = input("Choose an Option: ")
        if userCh in ['1', '2','3']:
            break
    if userCh == '1':
        register()
    elif userCh == '2':
        login()
    elif userCh == '3':
        print("Thank you for using the Program!")
        pause()
        return 0
    else:
        print("Invalid input Try again...")
        pause()
        main()

main()
