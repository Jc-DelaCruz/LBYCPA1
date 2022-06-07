from stanfordkarel import *

def forward():
    if front_is_clear():
        move()
def straight():
    while front_is_clear():
        forward()
def west():
    while not_facing_west():
        turn_left()
def north():
    while not_facing_north():
        turn_left()
def south():
    while not_facing_south():
        turn_left()
def east():
    while not_facing_east():
        turn_left()
def beeper():
    if no_beepers_present():
        put_beeper()

def origin():
    south()
    straight()
    west()
    straight()
    north()

def count():
    countVar = 0
    east()
    while front_is_clear():
        forward()
        countVar += 1
    # print(countVar)
    return countVar


def main():
    half_x, half_y = int(), int()
    x = count()

    isOdd = bool()
    if (x % 2) == 0:
        isOdd = False
    else:
        isOdd = True

    half_x = x / 2
    half_y = x / 2

    north()
    straight()
    west()

    if isOdd:
        for i in range(0,int(half_x+1)):
            forward()
        for i in range(0,int(half_y+1)):
            beeper()
            south()
            forward()
            west()
            forward()
        for i in range(0,int(half_x+1)):
            beeper()
            south()
            forward()
            east()
            forward()
        for i in range(0,int(half_y+1)):
            beeper()
            north()
            forward()
            east()
            forward()
        for i in range(0,int(half_x+1)):
            beeper()
            north()
            forward()
            west()
            forward()

    else:
        for j in range(0,int(half_x)):
            forward()
        for j in range(0,int(half_y)):
            beeper()
            south()
            forward()
            west()
            forward()
        for j in range(0,int(half_x)):
            beeper()
            south()
            forward()
            east()
            forward()
        for j in range(0,int(half_y)):
            beeper()
            north()
            forward()
            east()
            forward()
        for j in range(0,int(half_x)):
            beeper()
            north()
            forward()
            west()
            forward()

if __name__ == "__main__":
    run_karel_program()
