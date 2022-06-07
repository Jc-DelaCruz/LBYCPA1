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

def left():
    while not_facing_west():
        turn_left()

def up():
    while not_facing_north():
        turn_left()

def down():
    while not_facing_south():
        turn_left()

def right():
    while not_facing_east():
        turn_left()

def main():
    """Karel code goes here!"""

    x = 0
    y = 0
    while front_is_clear():
        move()
        x+=1
    up()
    while front_is_clear():
        move()
        y+=1
    left()
    straight()
    down()
    straight()
    # while x > 0:


if __name__ == "__main__":
    run_karel_program()

