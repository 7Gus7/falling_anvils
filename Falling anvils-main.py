from microbit import *
import random


def main():
    #Neverending while loop
    while True:

        #Start on the menu until player is ready
        show_menu()


        
        #Initialization
        x = 2             #Players location (starts in middle)
        fall_rate = 32    #Anvils fall down at this rate
        spawn_rate = 128  #Spawns a new row at this rate
        num_spawn = 1     #How many obstacles are spawned
        score = 0         #Score gained by hitting anvils from the side
        timer = ticks(running_time())

        #Put the player onscreen
        display.set_pixel(x, 4, 9)
        

        
        #Main gameplay loop
        while True:
            
            #Move player left
            if button_a.was_pressed() and x > 0:
                display.set_pixel(x, 4, 0)
                x -= 1

                #If we hit the side of an anvil, increase score
                if display.get_pixel(x, 4):
                    score += 1
                
                display.set_pixel(x, 4, 9)

            #Move player right
            if button_b.was_pressed() and x < 4:
                display.set_pixel(x, 4, 0)
                x += 1

                #If we hit the side of an anvil, increase score
                if display.get_pixel(x, 4):
                    score += 1
                
                display.set_pixel(x, 4, 9)
    

            #Timer is updated every centisecond and updates the board
            if timer != ticks(running_time()):
                timer = ticks(running_time())

                #Increase the difficulty every so often
                if timer % 300 == 0:
                    fall_rate = max(fall_rate//2, 2)
                    spawn_rate = max(spawn_rate//2, 4)
                    num_spawn = min(num_spawn + 1, 4)
                    

                #Every fall_rate seconds, we update the screen
                if timer % fall_rate == 0:
                    #Death check
                    if display.get_pixel(x, 3):
                        break
                        
                    #Move anvils down
                    fall(x)
                    

                #Depending on timer, spawn in a row of anvils
                spawn_row(timer, spawn_rate, num_spawn)
    

        #You lost, show score and then it 
        display.scroll("GG Score: " + str(score))
               



def ticks(ms):
    #ms to cs, for consistency in numbers
    return ms // 100




def show_menu():
    """
    Tells the player 'A To Start' and checks if the A button was
    pressed inbetween words so you aren't just sitting there waiting
    """

    while True:
        if button_a.was_pressed():
            break
            
        display.scroll("A")
        
        if button_a.was_pressed():
            break

        #Scrolling image of the word 'to'
        left_to = Image('99900:09000:09009:09090:09009')
        right_to = left_to.shift_left(1) + Image('00000:00000:00000:00009:00000')
        word_to = [left_to.shift_left(-5),
                   left_to.shift_left(-4),
                   left_to.shift_left(-3),
                   left_to.shift_left(-2),
                   left_to.shift_left(-1),
                   left_to,
                   right_to,
                   right_to.shift_left(1),
                   right_to.shift_left(2),
                   right_to.shift_left(3),
                   right_to.shift_left(4),
                   right_to.shift_left(5)]

        display.show(word_to, delay=150)
        if button_a.was_pressed():
            break
            
        display.scroll("Start ")


    #Once A is pressed, count down and then begin
    display.show(321, delay=600)
    display.clear()




def fall(x):
    """
    Goes through each pixel left to right & bottom to top,
    and shifts them downwards (without removing the player)
    """
    for row in reversed(range(5)):
        for column in range(5):
            if display.get_pixel(column, row) and row != 4:
                display.set_pixel(column, row, 0)
                display.set_pixel(column, row +1, 7)
            elif row == 4 and column != x:
                display.set_pixel(column, row, 0)




def spawn_row(timer, spawn_rate, num_spawn):
    """
    If it's time to spawn in a new row, we do so. Number of anvils
    spawned can very, and also they can sometimes stack
    """
    if timer % spawn_rate == 0:
        for led in range(num_spawn):
            display.set_pixel(random.randint(0, 4), 0, 7)




if __name__ == "__main__":
    main()