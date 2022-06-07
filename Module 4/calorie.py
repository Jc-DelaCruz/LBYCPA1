def BMI(height, weight):
    bmi = weight / height ** 2
    if (bmi < 16.5):
        return 'You are severly underweight. \nRecommended Calorie Intake: 2,400',bmi

    elif (bmi >= 16.5 and bmi <18.5):
        return 'You are underweight. \nRecommended Calorie Intake: 2,200',bmi

    elif (bmi >= 18.5 and bmi <25):
        return 'You are Healthy. \nRecommended Calorie Intake: 2,100',bmi

    elif (bmi >= 25 and bmi <30):
        return 'You are Overweight. \nRecommended Calorie Intake: 1,800',bmi

    elif (bmi >= 30):
        return 'You are Obese. \nRecommended Calorie Intake: 1,600',bmi

print("==BMI and Calorie Intake Calculator==\n")
print("This Program is for people who wants to try a Calorie Deficit diet and doesn't know what their Calorie Intake is.")
print("Fill out the form Below\n")
name = input("Enter your name:  ")
weight = float(input("Enter your Weight in Kilograms (kg): "))
height = float(input("Enter your Height in Meters (m): "))


print("\n\nHello, ", name, "\n")
line, bmi = BMI(height, weight)
print("Your BMI is: {} and {}".format(round(bmi, 2),line))


