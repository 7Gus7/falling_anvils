#import radio
#import music

#import math
import random

import time

from microbit import *


def main():
    # are we in the main menu?
    '''menu = True
    
    while menu:
        show_menu()
    '''

    x = 2    #players location
    fall_rate = 5    #falls down one pixel every x seconds
    spawn_rate = 5    #spawns a new row every x seconds
    num_spawn = 1    #how many objects are spawned
    timer = secs(time.ticks_ms())
    
    display.set_pixel(x, 4, 9)    #player
    
    while True:
        if button_a.was_pressed() and x > 0:
            display.set_pixel(x, 4, 0)
            x -= 1
            display.set_pixel(x, 4, 9)
        
        if button_b.was_pressed() and x < 4:
            display.set_pixel(x, 4, 0)
            x += 1
            display.set_pixel(x, 4, 9)



        if timer != secs(time.ticks_ms()):
            timer = secs(time.ticks_ms())

            #death check
            if display.get_pixel(x, 3):
                print("dead")

            #move anvils down
            for column in reversed(range(5)):
                for row in range(5):
                    if display.get_pixel(row, column) and column != 4:
                        display.set_pixel(row, column, 0)
                        display.set_pixel(row, column +1, 9)
                    elif column == 4 and row != x:
                        display.set_pixel(row, column, 0)

            #spawn in a new row of anvils
            if timer % spawn_rate == 0:
                for led in range(num_spawn):
                    display.set_pixel(random.randint(0, 4), 0, 9)


                        





def secs(ms):
    return ms // 1000



'''
def show_menu():
    display.show("MENU ", delay = 300)
    display.show("A ", delay = 300)
    
    # display 'To'
    display.show(Image('99900:09000:09090:09909:09090'), wait = False)
    sleep(600)
    display.show(" Start ", delay = 300)

'''



if __name__ == "__main__":
    main()