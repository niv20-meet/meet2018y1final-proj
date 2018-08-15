import turtle
import random
import time
#screen=turtle.screen
turtle.tracer(1, 0)  # This helps the turtle move more smoothly
distance= 20
SIZE_X = 800
SIZE_Y = 500
LEFT_EDGE = -400
turtle.setup(SIZE_X, SIZE_Y)  # Curious? It's the turtle window
# size.
TIME_STEP= 20
turtle.bgcolor("grey")
trash=turtle.Turtle()
trash_1=turtle.Turtle()
trash_2=turtle.Turtle()
trash_3=turtle.Turtle()


trash_pos=[trash, trash_1 , trash_2, trash_3]
player_pos=[]
questions=[]
trash_list=[]


for t in trash_pos:
    t.shape("square")
    t.penup()
    t.goto(400,0)
    t.pendown()
    

'''
def make_trash():
    new_trash=trash.clone()
    trash_list.append (new_trash)
    new_trash.goto (400,0)
'''
    
    


      
def move_trash():
    global trash
    my_pos = trash.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    trash.goto(x_pos-distance, y_pos)

    for trash in trash_list:
        trash.goto(-200,0)
        
     
        

    
        
    
if trash_3.pos()[0] <= LEFT_EDGE+20:
        print("you hit the edge")
        trash_3.hideturtle()
else:
    turtle.ontimer(move_trash,TIME_STEP) #<--Last line of function

space1 = 200
space2 = 50
space3 = -100
move_trash()
mario=turtle.Turtle()
turtle.register_shape("mario.gif")


