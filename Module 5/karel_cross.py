
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

def get_world_size():
    # This function will let Karel survey the world to determine its size. It will return with the size of the world.
    wsize = int(1)
    east()
    while front_is_clear():
        forward()
        wsize += 1
    return wsize

def draw_diagonal_rightdown(nbeepers):
    # This function will generate a downward diagonal line of beepers. Karel will move right then down as beepers are placed.
    # It will not put a beeper if a corner has already a beeper in it. Karel will stop if blocked ahead.

    used_beepers = 0
    while not_facing_east():
        turn_left()
    for i in range(nbeepers):
        if no_beepers_present():
            put_beeper()
            used_beepers += 1
        if i < nbeepers - 1:
            move()
            while not_facing_south():
                turn_left()
            if front_is_blocked():
                break
            move()
        while not_facing_east():
            turn_left()
        if front_is_blocked():
            break
    if nbeepers > 0 and no_beepers_present():
        put_beeper()
        used_beepers += 1
    return used_beepers

def draw_diagonal_rightup(nbeepers):
    # This function will generate a upward diagonal line of beepers. Karel will move right then up as beepers are placed.
    # It will not put a beeper if a corner has already a beeper in it. Karel will stop if blocked ahead.

    used_beepers = 0
    while not_facing_east():
        turn_left()
    for i in range(nbeepers):
        if no_beepers_present():
            put_beeper()
            used_beepers += 1
        if i < nbeepers - 1:
            move()
            while not_facing_north():
                turn_left()
            if front_is_blocked():
                break
            move()
        while not_facing_east():
            turn_left()
        if front_is_blocked():
            break
    if nbeepers > 0 and no_beepers_present():
        put_beeper()
        used_beepers += 1
    return used_beepers

def draw_horizontal_right(nbeepers):
    # This function will generate a horizontal line of beepers. Karel will move right as beepers are placed.
    # It will not put a beeper if a corner has already a beeper in it. Karel will stop if blocked ahead.

    used_beepers = 0
    while not_facing_east():
        turn_left()
    for i in range(nbeepers):
        if no_beepers_present():
            put_beeper()
            used_beepers += 1
        if i < nbeepers - 1:
            move()
        if front_is_blocked():
            break
    if nbeepers > 0 and no_beepers_present():
        put_beeper()
        used_beepers += 1
    return used_beepers

def draw_vertical_down(nbeepers):
    # This function will generate a vertical line of beepers. Karel will move down as beepers are placed.
    # It will not put a beeper if a corner has already a beeper in it. Karel will stop if blocked ahead.

    used_beepers = 0
    while not_facing_south():
        turn_left()
    for i in range(nbeepers):
        if no_beepers_present():
            put_beeper()
            used_beepers += 1
        if i < nbeepers - 1:
            move()
        if front_is_blocked():
            break
    if nbeepers > 0 and no_beepers_present():
        put_beeper()
        used_beepers += 1
    return used_beepers

def main():
    # Step 0: Initialize variables
    center_coord_x, center_coord_y = int(), int()
    beepers_used = int()

    # # Step 1: Determine world size
    world_size = get_world_size() # you have to implement the function above

    # # Step 2: Check if the world size is odd or even
    isOdd = bool()
    if (world_size % 2) == 0:
        isOdd = False
    else:
        isOdd = True

    # # Step 3: Compute for the center coordinates of the world
    center_coord_x = world_size / 2
    center_coord_y = world_size / 2

    #
    # # Step 4: Position Karel and generate the beeper lines
    beepers_used = 0
    if isOdd:
        north()
        straight()
        west()
        for i in range (0, center_coord_x):
            forward()
        beepers_used += draw_vertical_down(world_size)
        west()
        straight()
        north()
        for i in range (0, center_coord_y):
            forward()
        beepers_used += draw_horizontal_right(world_size)
    else:
        west()
        straight()
        beepers_used += draw_diagonal_rightup(world_size)
        west()
        straight()
        beepers_used += draw_diagonal_rightdown(world_size)

    #
    # # Step 5: Print the center coordinates and the number of beepers used
    get_world_size()
    if isOdd:
        print("\nCenter Coordinates is ", center_coord_x + 1,",", center_coord_y + 1)
    else:
        print("\nCenter Coordinates is ", center_coord_x + 0.5 ,",", center_coord_y + 0.5)
    print("Beepers Used is ", beepers_used)
    print("\nThe World Size is ", world_size, "x", world_size)

if __name__ == "__main__":
    run_karel_program()
