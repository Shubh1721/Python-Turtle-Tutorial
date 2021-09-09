import turtle
import time

turtle.bgcolor('black')
# turtle.color('red')
# turtle.shapesize(4,4,4)

player = turtle.Turtle()
player.shapesize(5,5,5)

def animate(color):
    player.color(color)
    player.shape('square')
    time.sleep(0.5)
    player.shape('circle')
    time.sleep(0.5)

player2 = player.clone()
def animate2(color):
    player2.color(color)
    player2.shape('square')
    time.sleep(0.5)
    player2.shape('circle')
    time.sleep(0.5)

while True:

    animate('red') 
    player2.goto(200,200)
    animate2("green")
    # player.goto(0,100)
    # animate('yellow')

turtle.mainloop()


'''

while True:
    turtle.color('red')
    turtle.shape('circle')
    time.sleep(0.5)

    turtle.color('green')
    turtle.shape('square')
    time.sleep(0.5)
    
    turtle.color('blue')
    turtle.shape('turtle')
    time.sleep(0.5)


'''