from random import randint
import turtle


t = turtle.Turtle()
wn = turtle.Screen()
t.shape('turtle')


#function to check if the turtle is still inside the screen
def isin(wn, t):
    left = -(wn.window_width()/2)
    right = wn.window_width()/2
    up = wn.window_height()/2
    down = -(wn.window_height()/2)
    
    turtleX = t.xcor()
    turtleY = t.ycor()
    stillin = True
    
    if turtleX < left or turtleX > right:
        stillin = False
    if turtleY < down and turtleY > up:
        stillin = False
    return stillin


#set some colours for turtle's trail
red = 0
green = 20
blue = 40


while isin:
	#turtle turns left and right randomly
    dice = randint(1, 2)
    if dice == 1:
        t.left(90)
    elif dice == 2:
        t.right(90)
    turtle.colormode(cmode = 255)
    t.pencolor(red, green, blue)
	
    #changing colors
    if red> 254:
        red = 0
    if green > 254:
        green = 0
    if blue> 254:
        blue = 0
    red+=1
    green+=1
    blue+=1
    t.forward(5)
	
turtle.exitonclick()