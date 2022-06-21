# Module which would ask the user if they want to use a first term or second term gpa
# included in the module: if and else for the first and second functions
# import first and second functions

def course_gpa_calculator():

    choices_1st = ('FNDMATH', 'BASPHYS', 'BASCHEM', 'FNDSTAT', 'GEARTAP')

    choices_2nd = ('CALENG1', 'COEDISC', 'PROLOGI', 'LBYCPA1',
                   'LBYEC2A', 'GESTSOC', 'GERIZAL', 'LCASEAN')
    choices_term = ('FIRST TERM', '1ST TERM', 'FIRST', '1ST', '1',
                    'SECOND TERM', '2ND TERM', 'SECOND', '2ND', '2')
    raw_gpa = float(4.0)
    clear()
    print("=========================================================")
    print("Welcome to the CpE Frosh Companion course GPA calculator!")
    print("=========================================================")
    # TERM CHOOSING
    term = str(input("\nPlease choose a term: "))
    term = term.upper()
    # CHECKING OF TERMS
    if term in choices_term:
        # TERM 1
        if term == choices_term[0] or term == choices_term[1] or term == choices_term[2] or term == choices_term[3] or term == choices_term[4]:
            choice = str(
                input("\nPlease enter a course code for the 1nd term calculator: "))
            choice = choice.upper()
            # COURSE CHECKING
            if choice in choices_1st:
                # FNDMATH
                if choice == choices_1st[0]:
                    fndmath = ['quizzes', 'activities',
                               'seatworks', 'finals', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_1st[0], "\n")

                    fndmath[0] = float(
                        input("Input total Quizzes grade: "))
                    fndmath[1] = float(
                        input("Input total Activities grade: "))
                    fndmath[2] = float(
                        input("Input total Seatworks grade: "))
                    fndmath[3] = float(
                        input("Input Final Examination grade: "))
                    fndmath[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((fndmath[0] * 0.30) + (fndmath[1] * 0.2) +
                             (fndmath[2] * 0.15) + (fndmath[3] * 0.30) + (fndmath[4] * 0.05))
                # BASPHYS
                elif choice == choices_1st[1]:
                    basphys = ['quizzes', 'problem sets',
                               'finals', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_1st[1], "\n")

                    basphys[0] = float(
                        input("Input total Quizzes grade: "))
                    basphys[1] = float(
                        input("Input total Problem Sets grade: "))
                    basphys[2] = float(
                        input("Input Final Examination grade: "))
                    basphys[3] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((basphys[0] * 0.35) + (basphys[1] * 0.25) +
                             (basphys[2] * 0.35) + (basphys[3] * 0.05))
                # BASCHEM
                elif choice == choices_1st[2]:
                    baschem = ['quizzes', 'seatworks',
                               'finals', 'project', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_1st[2], "\n")

                    baschem[0] = float(
                        input("Input total Quizzes grade: "))
                    baschem[1] = float(
                        input("Input total seatworks grade: "))
                    baschem[2] = float(
                        input("Input Final Examination grade: "))
                    baschem[3] = float(
                        input("Input Term-End Project grade: "))
                    baschem[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((baschem[0] * 0.30) + (baschem[1] * 0.2) +
                             (baschem[2] * 0.15) + (baschem[3] * 0.30) + (baschem[4] * 0.05))
                # FNDSTAT
                elif choice == choices_1st[3]:
                    fndstat = ['quizzes', 'finals',
                               'Collab_day', 'recitation', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_1st[3], "\n")

                    fndstat[0] = float(
                        input("Input total Quizzes grade: "))
                    fndstat[1] = float(
                        input("Input Final Examination grade: "))
                    fndstat[2] = float(
                        input("Input Collab Day grade: "))
                    fndstat[3] = float(
                        input("Input Recitation grade: "))
                    fndstat[4] = float(
                        input("Input Teacher's Evaluation grade"))

                    grade = ((fndstat[0] * 0.40) + (fndstat[1] * 0.35) +
                             (fndstat[2] * 0.1) + (fndstat[3] * 0.1) + (fndstat[4] * 0.05))
                # GEARTAP
                elif choice == choices_1st[4]:
                    geartap = ['reflections', 'individual activities',
                               'personal assessment', 'reporting', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_1st[4], "\n")

                    geartap[0] = float(
                        input("Input overall Reflections grade: "))
                    geartap[1] = float(
                        input("Input overall Individual Activities grade: "))
                    geartap[2] = float(
                        input("Input Personal Assessment grade: "))
                    geartap[3] = float(
                        input("Input Group Reporting grade: "))
                    geartap[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((geartap[0] * 0.25) + (geartap[1] * 0.25) +
                             (geartap[2] * 0.20) + (geartap[3] * 0.25) + (geartap[4] * 0.05))

                if grade >= 94 and grade <= 100:
                    gpa = raw_gpa
                elif grade >= 88 and grade < 94:
                    gpa = raw_gpa - 0.5
                elif grade >= 82 and grade < 88:
                    gpa = raw_gpa - 1.0
                elif grade >= 75 and grade < 82:
                    gpa = raw_gpa - 1.5
                elif grade >= 69 and grade < 75:
                    gpa = raw_gpa - 2.0
                elif grade >= 62 and grade < 69:
                    gpa = raw_gpa - 2.5
                elif grade >= 55 and grade < 62:
                    gpa = raw_gpa - 3.0
                else:
                    gpa = raw_gpa - 4.0
                print("\nYour", choice, "gpa is:", gpa, "\n")

            else:
                print("Invalid Course Code!!!")
        # TERM 2
        elif term == choices_term[5] or term == choices_term[6] or term == choices_term[7] or term == choices_term[8] or term == choices_term[9]:

            choice = str(
                input("\nPlease enter a course code for the 2nd term calculator: "))
            choice = choice.upper()
            # COURSE CHECKING
            if choice in choices_2nd:
                # CALENG1
                if choice == choices_2nd[0]:
                    caleng1 = ['lq', 'finals', 'activities',
                               'project', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[0], "\n")

                    caleng1[0] = float(
                        input("Input overall Long Quizzes grade: "))
                    caleng1[1] = float(
                        input("Input Final Examination grade: "))
                    caleng1[2] = float(
                        input("Input total activities grades: "))
                    caleng1[3] = float(
                        input("Input Class-produced Project grade: "))
                    caleng1[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((caleng1[0] * 0.55) + (caleng1[1] * 0.30) +
                             (caleng1[2] * 0.05) + (caleng1[3] * 0.05) + (caleng1[4] * 0.05))

                    if grade >= 94 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 88 and grade < 94:
                        gpa = raw_gpa - 0.5
                    elif grade >= 82 and grade < 88:
                        gpa = raw_gpa - 1.0
                    elif grade >= 75 and grade < 82:
                        gpa = raw_gpa - 1.5
                    elif grade >= 69 and grade < 75:
                        gpa = raw_gpa - 2.0
                    elif grade >= 62 and grade < 69:
                        gpa = raw_gpa - 2.5
                    elif grade >= 55 and grade < 62:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour CALENG1 gpa is:", gpa, "\n")

                # COEDISC
                elif choice == choices_2nd[1]:
                    coedisc = ['quiz', 'written_reports',
                               'project', 'finals', 'evaluation']

                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[1], "\n")

                    coedisc[0] = float(input("Input overall Quizzes grade: "))
                    coedisc[1] = float(input("Input Written Reports grade: "))
                    coedisc[2] = float(input("Input Term Project grade: "))
                    coedisc[3] = float(
                        input("Input Final Examination grade: "))
                    coedisc[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((coedisc[0] * 0.25) + (coedisc[1] * 0.20) +
                             (coedisc[2] * 0.25) + (coedisc[3] * 0.25) + (coedisc[4] * 0.05))

                    if grade >= 95 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 90 and grade < 95:
                        gpa = raw_gpa - 0.5
                    elif grade >= 85 and grade < 90:
                        gpa = raw_gpa - 1.0
                    elif grade >= 80 and grade < 85:
                        gpa = raw_gpa - 1.5
                    elif grade >= 75 and grade < 80:
                        gpa = raw_gpa - 2.0
                    elif grade >= 70 and grade < 75:
                        gpa = raw_gpa - 2.5
                    elif grade >= 65 and grade < 70:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour COEDISC gpa is:", gpa, "\n")

                # PROLOGI
                elif choice == choices_2nd[2]:
                    prologi = ['assignments', 'quizes',
                               'project', 'finals', 'evaluation']
                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[2], "\n")

                    prologi[0] = float(
                        input("Input overall Assignments grade: "))
                    prologi[1] = float(input("Input overall Quizzes grade: "))
                    prologi[2] = float(input("Input Final Project grade: "))
                    prologi[3] = float(
                        input("Input Final Examination grade: "))
                    prologi[4] = float(
                        input("Input Teacher's Evaluation grade: "))

                    grade = ((prologi[0] * 0.2) + (prologi[1] * 0.25) +
                             (prologi[2] * 0.25) + (prologi[3] * 0.25) + (prologi[4] * 0.05))

                    if grade >= 95 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 90 and grade < 95:
                        gpa = raw_gpa - 0.5
                    elif grade >= 85 and grade < 90:
                        gpa = raw_gpa - 1.0
                    elif grade >= 80 and grade < 85:
                        gpa = raw_gpa - 1.5
                    elif grade >= 75 and grade < 80:
                        gpa = raw_gpa - 2.0
                    elif grade >= 70 and grade < 75:
                        gpa = raw_gpa - 2.5
                    elif grade >= 65 and grade < 70:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour PROLOGI gpa is:", gpa, "\n")

                # LBYCPA1
                elif choice == choices_2nd[3]:
                    lbycpa1 = ['Lab_Exp', 'Eng_nb', 'project', 'prac_exam']

                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[3])

                    lbycpa1[0] = float(
                        input("Input overall Laboratory Activity grade: "))
                    lbycpa1[1] = float(
                        input("Input Engineering Notebook grade: "))
                    lbycpa1[2] = float(input("Input Project grade: "))
                    lbycpa1[3] = float(
                        input("Input overall Practical Exam grade: "))

                    if grade >= 96 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 92 and grade < 96:
                        gpa = raw_gpa - 0.5
                    elif grade >= 88 and grade < 92:
                        gpa = raw_gpa - 1.0
                    elif grade >= 83 and grade < 88:
                        gpa = raw_gpa - 1.5
                    elif grade >= 78 and grade < 83:
                        gpa = raw_gpa - 2.0
                    elif grade >= 74 and grade < 78:
                        gpa = raw_gpa - 2.5
                    elif grade >= 70 and grade < 74:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour LBYCPA1 gpa is:", gpa, "\n")

                # LBYEC2A
                elif choice == choices_2nd[4]:
                    lbyec2a = ['lab_activities',
                               'pracexam1', 'pracexam2', 'project']

                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[4], "\n")

                    lbyec2a[0] = float(
                        input("Input Overall Lab Activities grade: "))
                    lbyec2a[1] = float(input("Input Practical Exam 1 grade: "))
                    lbyec2a[2] = float(input("Input Practical Exam 2 grade: "))
                    lbyec2a[3] = float(input("Input Project grade: "))

                    if grade >= 96 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 92 and grade < 96:
                        gpa = raw_gpa - 0.5
                    elif grade >= 88 and grade < 92:
                        gpa = raw_gpa - 1.0
                    elif grade >= 83 and grade < 88:
                        gpa = raw_gpa - 1.5
                    elif grade >= 78 and grade < 83:
                        gpa = raw_gpa - 2.0
                    elif grade >= 74 and grade < 78:
                        gpa = raw_gpa - 2.5
                    elif grade >= 70 and grade < 74:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour LBYEC2A gpa is:", gpa, "\n")

                # GESTSOC
                elif choice == choices_2nd[5]:
                    gestsoc = ['indiv_report', 'group_report',
                               'project', 'Participation_Presentation']

                    print("\nThis is a course GPA calculator for: ",
                          choices_2nd[5])

                    gestsoc[0] = float(
                        input("Input overall Individual Report grade: "))
                    gestsoc[1] = float(
                        input("Input overall Group Report grade: "))
                    gestsoc[2] = float(
                        input("Input Final Course Output grade: "))
                    gestsoc[3] = float(
                        input("Input Class Participation and Group Presentation grade: "))

                    grade = ((gestsoc[0] * 0.3) + (gestsoc[1] * 0.25) +
                             (gestsoc[2] * 0.25) + (gestsoc[3] * 0.2))

                    if grade >= 96 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 91 and grade < 96:
                        gpa = raw_gpa - 0.5
                    elif grade >= 87 and grade < 91:
                        gpa = raw_gpa - 1.0
                    elif grade >= 83 and grade < 87:
                        gpa = raw_gpa - 1.5
                    elif grade >= 79 and grade < 83:
                        gpa = raw_gpa - 2.0
                    elif grade >= 75 and grade < 79:
                        gpa = raw_gpa - 2.5
                    elif grade >= 70 and grade < 75:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour GESTSOC gpa is:", gpa, "\n")

                # GERIZAL
                elif choice == choices_2nd[6]:
                    gerizal = ['advoc', 'script', 'group_activity',
                               'integpapers', 'reaction_paper', 'bonuses']

                    print("\nThis is a course GPA calculator for:",
                          choices_2nd[6], "\n")
                    grade = 0

                    gerizal[0] = float(
                        input("Input overall Advocay Campaign grade: "))
                    gerizal[1] = float(input("Input overall Script grad: "))
                    gerizal[2] = float(
                        input("Input overall Group Activity grade: "))
                    gerizal[3] = float(
                        input("Input overall Integration Paper grade: "))
                    gerizal[4] = float(input("Input Reaction Paper grade:"))
                    gerizal[5] = float(
                        input("Input overall Recitation and Book Report grade: "))

                    for x in gerizal:
                        grade += x

                    if grade >= 187 and grade <= 200:
                        gpa = raw_gpa
                    elif grade >= 174 and grade < 187:
                        gpa = raw_gpa - 0.5
                    elif grade >= 161 and grade < 174:
                        gpa = raw_gpa - 1.0
                    elif grade >= 148 and grade < 161:
                        gpa = raw_gpa - 1.5
                    elif grade >= 135 and grade < 148:
                        gpa = raw_gpa - 2.0
                    elif grade >= 122 and grade < 135:
                        gpa = raw_gpa - 2.5
                    elif grade >= 109 and grade < 122:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour GERIZAL gpa is:", gpa, "\n")

                # LCASEAN
                elif choice == choices_2nd[7]:
                    lcasean = ['cs11', 'cs2', 'presentation',
                               'essay', 'participation']

                    print("\n This is a course GPA calculator for:",
                          choices_2nd[7], "\n")

                    lcasean[0] = float(input("Input Case Study 1 grade: "))
                    lcasean[1] = float(input("Input Case Study 2 grade: "))
                    lcasean[2] = float(
                        input("Input Case Presentation grade: "))
                    lcasean[3] = float(input("Input Reflective Essay grade: "))
                    lcasean[4] = float(
                        input("Input Class Participation grade: "))

                    grade = ((lcasean[0] * 0.3) + (lcasean[1] * 0.35) +
                             (lcasean[2] * 0.15) + (lcasean[3] * 0.1) + (lcasean[4] * 0.01))

                    if grade >= 97 and grade <= 100:
                        gpa = raw_gpa
                    elif grade >= 93 and grade < 97:
                        gpa = raw_gpa - 0.5
                    elif grade >= 89 and grade < 93:
                        gpa = raw_gpa - 1.0
                    elif grade >= 85 and grade < 89:
                        gpa = raw_gpa - 1.5
                    elif grade >= 80 and grade < 85:
                        gpa = raw_gpa - 2.0
                    elif grade >= 75 and grade < 80:
                        gpa = raw_gpa - 2.5
                    elif grade >= 70 and grade < 75:
                        gpa = raw_gpa - 3.0
                    else:
                        gpa = raw_gpa - 4.0
                    print("\nYour LCASEAN gpa is:", gpa, "\n")
            else:
                print("Invalid Course Code")
    else:
        print("\nInvalid Input!")

    # RETURN TO MAIN MENU PROMPT
    menu = str(input("\nDo you want to return to the menu y/n? "))
    menu = menu.lower()
    if menu == 'y':
        pause()
        course_gpa_calculator()
    elif menu == 'n':
        print("\nThank you for using the CpE Frosh Companion GPA Calculator!\n")
        pause()
        return 0

# OVERALL or TERM GPA CALCULATOR
# INPUT: INDIVIDUAL GPA OF EACH TERM
# OUTPUT: TERM GPA(two decimal places)

def term_gpa_calculator():

    choices_term = ('FIRST TERM', '1ST TERM', 'FIRST', '1ST', '1',
                    'SECOND TERM', '2ND TERM', 'SECOND', '2ND', '2')
    clear()
    print("==========================================================")
    print("Welcome to the CpE Frosh Companion term GPA calculator!")
    print("==========================================================")

    # CHOOSING OF TERM
    term = str(input("\nPlease choose a term: "))
    term = term.upper()

    if term in choices_term:
        # TERM 1
        if term == choices_term[0] or term == choices_term[1] or term == choices_term[2] or term == choices_term[3] or term == choices_term[4]:
            choice = str(
                input("\nDo you want to view your previous GPA y/n? "))
            choice = choice.lower()
            if choice == 'n':
                possible_gpa = (0, 1, 1.5, 2, 2.5, 3, 3.5, 4)

                try:
                    file = open("term1_gpa_calculator.txt", "w")
                except FileNotFoundError:
                    return "Error: File is not accessible!"
                print("\nPlease input the following: ")
                print("Possible Values:", possible_gpa)
                while True:
                    try:
                        fndmath = float(input("\nWhat is your FNDMATH gpa? "))
                        if not(fndmath in possible_gpa):
                            raise ValueError('Not within range')

                        basphys = float(input("What is your BASPHYS gpa? "))
                        if not(basphys in possible_gpa):
                            raise ValueError('Not within range')

                        baschem = float(input("What is your BASCHEM gpa? "))
                        if not(baschem in possible_gpa):
                            raise ValueError('Not within range')

                        fndstat = float(input("What is your FNDSTAT gpa? "))
                        if not(fndstat in possible_gpa):
                            raise ValueError('Not within range')

                        geartap = float(input("What is your GEARTAP gpa? "))
                        if not(geartap in possible_gpa):
                            raise ValueError('Not within range')

                        break
                    except:
                        raise TypeError('not a valid number!')

                overall_gpa = (((fndmath * 5) + (basphys * 3) + (baschem * 3) + (fndstat * 3) +
                                (geartap * 3))/17)

                overall_gpa = "{:.2f}".format(overall_gpa)
                print(" \nYour first term GPA is:", overall_gpa)
                file.write("Your first term GPA is: ")
                file.write(overall_gpa)
                file.close()

            elif choice == 'y':
                file = open("term1_gpa_calculator.txt")
                print("\n")
                file = file.read()
                print(file)
            else:
                print("\nInvalid Input!")
        # TERM 2
        elif term == choices_term[5] or term == choices_term[6] or term == choices_term[7] or term == choices_term[8] or term == choices_term[9]:
            choice = str(
                input("\nDo you want to view your previous GPA y/n? "))
            choice = choice.lower()

            if choice == 'n':
                possible_gpa = (0, 1, 1.5, 2, 2.5, 3, 3.5, 4)

                try:
                    file = open("term2_gpa_calculator.txt", "w")
                except FileNotFoundError:
                    return "Error: File is not accessible!"
                print("\nPlease input the following: ")
                print("Possible Values:", possible_gpa)
                while True:
                    try:
                        caleng1 = float(input("\nWhat is your Caleng1 gpa? "))
                        if not(caleng1 in possible_gpa):
                            raise ValueError('Not within range')

                        coedisc = float(input("What is your Coedisc gpa? "))
                        if not(coedisc in possible_gpa):
                            raise ValueError('Not within range')

                        prologi = float(input("What is your Prologi gpa? "))
                        if not(prologi in possible_gpa):
                            raise ValueError('Not within range')

                        lbycpa1 = float(input("What is your Lbycpa1 gpa? "))
                        if not(lbycpa1 in possible_gpa):
                            raise ValueError('Not within range')

                        lbyec2a = float(input("What is your Lbyec2a gpa? "))
                        if not(lbyec2a in possible_gpa):
                            raise ValueError('Not within range')

                        gestsoc = float(input("What is your Gestsoc gpa? "))
                        if not(gestsoc in possible_gpa):
                            raise ValueError('Not within range')

                        gerizal = float(input("What is your Gerizal gpa? "))
                        if not(gerizal in possible_gpa):
                            raise ValueError('Not within range')

                        lcasean = float(input("What is your Lcasean gpa? "))
                        if not(lcasean in possible_gpa):
                            raise ValueError('Not within range')

                        break
                    except:
                        raise TypeError('not a valid number!')

                overall_gpa = (((caleng1 * 3) + (coedisc * 1) + (prologi * 2) + (lbycpa1 * 2) +
                                (lbyec2a * 1) + (gestsoc * 3) + (gerizal * 3) + (lcasean * 3)) / 18)
                overall_gpa = "{:.2f}".format(overall_gpa)
                print(" \nYour second term GPA is:", overall_gpa)
                file.write("Your second term gpa is: ")
                file.write(overall_gpa)
                file.close()

            elif choice == 'y':
                file = open("term2_gpa_calculator.txt")
                print("\n")
                file = file.read()
                print(file)
            else:
                print("\nInvalid Input!")
        else:
            print("Invalid Input!")

    menu = str(
        input("\nDo you want to go back to the gpa calculator menu y/n? "))
    menu = menu.lower()
    if menu == 'y':
        term_gpa_calculator()
    elif menu == 'n':
        print("\nThank you for using the CpE Frosh Companion GPA Calculator!\n")
        return


# MAIN FUNCTION ----------------------------------
def gpa_menu():
    # clear()
    print("=====================")
    print("GPA Calculator")
    print("=====================")
    print("1 - Term GPA Calculator")
    print("2 - Course GPA Calculator")
    print("3 - Exit")
    while True:
        print()
        choice = input("Choose a Term: ")
        if choice in ['1','2','3']:
            break
        
    if choice == '1':
        term_gpa_calculator()
        flowchartExit()


    elif choice == '2':
        course_gpa_calculator()
        flowchartExit()


    elif choice == '3':
        print("Thank you for using the Program!")
        return 0

    else:
        print("Invalid Input... Try Again..")
        # pause()
        gpa_menu()

gpa_menu()