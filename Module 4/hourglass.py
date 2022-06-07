from stanfordkarel import *

def forward():
    if front_is_clear():
        move()
def straight():
    while front_is_clear():
        forward()
def straightb():
    while front_is_clear():
        beeper()
        forward()
        beeper()
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

def transition():
    north()
    straight()
    west()
    straight()
    east()
    straightb()
    west()
    straight()
    south()

def next():
    south()
    straight()
    west()
    straight()
    north()

def main():
    """ Karel code goes here! """
    #pyramid from bottom
    if front_is_blocked():
        beeper()
        return
    x=0
    z=0
    v=0
    beeper()
    while front_is_clear():
        forward()
        beeper()
        x+=1
    next()
    forward()
    east()
    if x<=2:
        return
    y=1
    z=x-1
    pyramid = 0 #switch for bottom or top
    while True:
        east()
        for i in range(int(y)-1):
            forward()
        for i in range(int(z)):
            forward()
            beeper()
        next()
        if pyramid == 0:
            north()
        elif pyramid == 1:
            straight()
            south()

        if pyramid == 0:
            v+=1
            for i in range(v+1):
                forward()
        elif pyramid == 1:
            v+=1
            for i in range(v):
                forward()

        if z==1:#After a pyramid
            y=-1
            z=x+3
            v=0
            pyramid +=1
            if pyramid == 1:
                transition()
            else:
                return
        z-=2
        y+=1
        if z == 0:
            y=0
            z=x+1
            v=0
            pyramid +=1
            if pyramid == 1:
                transition()
            else:
                return

   

if __name__ == "__main__":
    run_karel_program()
