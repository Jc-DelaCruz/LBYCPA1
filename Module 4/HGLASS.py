# -*- coding: utf-8 -*-
"""
Author: J4yl0rd
No copy pls
"""
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
def nextInstance():
    east()
    forward()
    north()
    forward()
    beeper()
def main():
    """ Karel code goes here! """
    x = 0
    y = 0
    beeper()
    while front_is_clear():
        forward()
        x+=1
    north()
    while front_is_clear():
        forward()
        y+=1
    west()
    straight()
    south()
    straight()
    while x > 0:
        east()
        for i in range(x):
            beeper()
            forward()
            beeper()
        north()
        for i in range(y):
            forward()
        west()
        for i in range(x):
            beeper()
            forward()
            beeper()
        south()
        for i in range(y):
            forward()
        y-=2
        x-=2
        nextInstance()
if __name__ == "__main__":
    run_karel_program()
