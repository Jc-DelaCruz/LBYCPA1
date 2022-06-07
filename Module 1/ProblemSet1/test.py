def raw2grade(score):
score = float(input("DLSU GPA Raw Grade Grade Calculator: "))



if not (type(score) is int or type(score) is float): #It verifies a correct input
#     raise TypeError("Input not a valid number")
#     print("Input not a valid number")

elif score > 100 or score < 0:
#     raise ValueError("Raw score must not be greater than 100 nor less than 0")
#     print("Raw score must not be greater than 100 nor less than 0")

else:
    print("Valid Grade -- Calculating...")
    print("\n")

#     print(raw2grade(score))
    if score >= 96 and score <= 100:
        print("Your Grade Equivalent is ", gpa4)
    elif score >= 92 and score <= 96:
        print("Your Grade Equivalent is ", gpa3_5)
    elif score >= 88 and score <= 92:
        print("Your Grade Equivalent is ", gpa3)
    elif score >= 83 and score <= 88:
        print("Your Grade Equivalent is ", gpa2_5)
    elif score >= 77 and score <= 83:
        print("Your Grade Equivalent is ", gpa2)
    elif score >= 74 and score <= 77:
        print("Your Grade Equivalent is ", gpa1_5)
    elif score >= 70 and score <= 74:
        print("Your Grade Equivalent is ", gpa1)
    else:
        print("Your Grade Equivalent is 0.0")

#     return gpa # Make sure to assign the result to the gpa variable
