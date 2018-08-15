import turtle
import random
import time

turtle.speed(0)
#screen=turtle.screen
# This helps the turtle move more smoothly
distance= 5
SIZE_X = 800
SIZE_Y = 500
LEFT_EDGE = -400
turtle.setup(SIZE_X, SIZE_Y)  # Curious? It's the turtle window
# size.
TIME_STEP= 20
turtle.bgcolor("grey")
trash=turtle.Turtle()
trash.shape("square")
player_pos=[]
questions=[]
trash_list=[]
mario = turtle.Turtle()
mario.penup()
mario.speed(1)
mario.left(90)

jumping = False
jump_time = 0
falling = False
falling_time = 0

def jump():
    global jumping, jump_time
    if not jumping and not falling:
        jump_time = 10
        jumping = True

trash.hideturtle()
trash.penup()
trash.speed(0)
trash.goto(400,0)
trash.showturtle()
trash.speed(2)

def is_in_range(point, lower, upper):
    return point >= lower and point <= upper

while True:
    mx, my = mario.pos()
    tx, ty = trash.pos()
    
    if is_in_range(mx, tx-2, tx+2) and is_in_range(my, ty-2, ty+2):
        quit()
    
    if trash.pos()[0] <= -400:        
        trash.hideturtle()
        trash.penup()
        trash.speed(0)
        trash.goto(400,0)
        trash.showturtle()
        trash.speed(2)
        
    turtle.onkeypress(jump, 'Up')
    turtle.listen()
        
    if jumping:
        mario.forward(5)
        jump_time -= 1
        if jump_time == 0:
            falling = True
            falling_time = 10
            jumping = False
            
    elif falling:
        mario.back(5)
        falling_time -= 1
        if falling_time == 0:
                falling = False
            
    if falling or jumping:
        my_pos = trash.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        trash.goto(x_pos-distance*5, y_pos)
    else:
        my_pos = trash.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        trash.goto(x_pos-distance, y_pos)
x


