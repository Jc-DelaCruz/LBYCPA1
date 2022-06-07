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
def downLeft():
    south()
    forward()
    west()
    straight()
def get_world_size():
    wsize = int(1)
    north()
    while front_is_clear():
        forward()
        wsize += 1
    return wsize

def main():
    # Dictionary data for a 7x7 world
    pix_7x7 = {
        'Row 1': (0,0,0,0,0,0,0),
        'Row 2': (0,1,1,0,1,1,0),
        'Row 3': (0,1,1,0,1,1,0),
        'Row 4': (0,0,0,0,0,0,0),
        'Row 5': (0,1,0,0,0,1,0),
        'Row 6': (0,0,1,1,1,0,0),
        'Row 7': (0,0,0,0,0,0,0)
    }

    # Dictionary data for a 40x40 world
    pix_40x40 = {
        'Row 1':  (0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0),
        'Row 2':  (0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0),
        'Row 3':  (0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0),
        'Row 4':  (0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0),
        'Row 5':  (0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0),
        'Row 6':  (0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0),
        'Row 7':  (0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0),
        'Row 8':  (0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0),
        'Row 9':  (0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0),
        'Row 10': (0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0),
        'Row 11': (0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0),
        'Row 12': (0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0),
        'Row 13': (0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0),
        'Row 14': (0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0),
        'Row 15': (0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0),
        'Row 16': (0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0),
        'Row 17': (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0),
        'Row 18': (0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0),
        'Row 19': (0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0),
        'Row 20': (0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0),
        'Row 21': (0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0),
        'Row 22': (0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0),
        'Row 23': (0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0),
        'Row 24': (0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0),
        'Row 25': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 26': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 27': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 28': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 29': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 30': (0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0),
        'Row 31': (0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0),
        'Row 32': (0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0),
        'Row 33': (0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0),
        'Row 34': (0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0),
        'Row 35': (0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0),
        'Row 36': (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0),
        'Row 37': (0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0),
        'Row 38': (0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),
        'Row 39': (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
        'Row 40': (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    }
    counter = 0
    worldSize = get_world_size()
    print(worldSize)

    if worldSize == 7:
       for rows, values in pix_7x7.items():
            for i in values:
                east()
                if i == 1:
                    paint_corner(PINK)
                    forward()
                elif i == 0:
                    forward()
                    if counter > len(pix_7x7[rows]) - 2:
                        downLeft()
                counter+=1
            counter = 0

    elif worldSize == 40:
        for rows, values in pix_40x40.items():
            # print("==",len(pix_40x40[rows]))
            for i in values:
                east()
                if i == 1:
                    paint_corner(PINK)
                    forward()
                elif i == 0:
                    forward()
                    if counter > len(pix_40x40[rows]) - 2:
                        downLeft()
                print("--",counter)
                counter+=1
            counter = 0

if __name__ == "__main__":
    run_karel_program()
