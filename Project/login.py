import os

def clear():
    os.system('cls')

def pause():
    os.system("pause")

def gpa_calculator():
    print("Loading... GPA Calculator Function ---")
    pass

def flowchart():
    print("Loading... Flowchart Function ---")
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
    while True:
        print()
        userCh = input("Choose an Option: ")
        if userCh in ['1', '2', '3']:
            break
    if userCh == '1':
        gpa_calculator()
    elif userCh == '2':
        flowchart()
    elif userCh == '3':
        help_desk()
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
    print()
    while True:
        print()
        userCh = input("Choose an Option: ")
        if userCh in ['1', '2']:
            break
    if userCh == '1':
        register()
    elif userCh == '2':
        login()
    else:
        print("Invalid input Try again...")
        pause()
        main()

main()
