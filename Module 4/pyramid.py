# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

def next():
    south()
    straight()
    west()
    straight()
    north()

def main():
    """ Karel code goes here! """
    if front_is_blocked():
        beeper()
        return
    x=0 #distance counter
    z=0 #beepers for that leve
    v=0
    beeper()
    while front_is_clear():
        forward()
        beeper()
        x+=1
    next()
    forward()
    east()
    y=1
    z=x-1
    while True:
        for i in range(int(y)-1):
            forward()
        for i in range(int(z)):
            forward()
            beeper()
        straight()
        south()
        straight()
        west()
        straight()
        north()
        v+=1
        for i in range(v+1):
            forward()
        east()
        if z==1:
            return
        z-=2
        y+=1
        if z == 0:
            return
        if z==1:
            return
    next()

if __name__ == "__main__":
    run_karel_program()
