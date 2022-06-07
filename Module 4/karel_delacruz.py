# KAREL HOURGLASS
# Dela Cruz -- 12195758
from stanfordkarel import *

def forward():
    if front_is_clear():
        move()
def straight():
    while front_is_clear():
        forward()
def beeper():
    if no_beepers_present():
        put_beeper()
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

def next():
    south()
    straight()
    west()
    straight()
    north()

def count2():
    countVar = 0
    west()
    while front_is_clear():
        forward()
        beeper()
        countVar += 1
    # print(countVar)
    return countVar

def count1():
    countVar = 0
    east()
    while front_is_clear():
        forward()
        beeper()
        countVar += 1
    # print(countVar)
    return countVar

def staircase1():
    x = count1()
    b = x - 2
    next()
    # -- Start of Staircase --
    while x >= 0:
        beeper()
        north()
        forward()
        east()
        forward()
        for i in range (0,b-1):
            forward()
            beeper()
        west()
        for i in range (0,b-1):
            forward()
        b -= 2  #b -= 2
        x -= 1

def staircase2():
    x = count2()
    b = x - 2
    # -- Start of Staircase --
    while x >= 0:
        beeper()
        south()
        forward()
        east()
        forward()
        for i in range (0,b-1):
            forward()
            beeper()
        west()
        for i in range (0,b-1):
            forward()
        b -= 2
        x -= 1

def main():
    """ Karel code goes here! """
    staircase1()
    staircase2()

if __name__ == "__main__":
    run_karel_program()
