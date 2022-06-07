def color_mix(color1, color2):

    if color1 == "red" and color2 == "blue":
        result = "purple"
    elif color1 == "blue" and color2 =="yellow":
        result = "green"
    elif color1 == "red" and color2 =="yellow":
        result = "orange"
    else
        result = "error"
    return result

print("COLOR MIXER: Input either red, blue, or yellow\n\n")

color1= str(input("Input 1st Color: "))
color2= str(input("Input 2nd Color: "))

result = color_mix(color1, color2)

print("The secondary color is", result)
