import turtle
import time


turtle.bgcolor('black')
# pen = turtle.Turtle()
class Player(turtle.Turtle):
    def __init__(self) :
        turtle.Turtle.__init__(self)
        self.shapesize(5,5,5)
        self.shape('circle')
        self.color('deepskyblue')
        # self.frame = ['circle','square']
    def animate(self):
        # self.frame
        self.shape('square')
        time.sleep(0.5)
        self.shape('circle')
        time.sleep(0.5)

player1 = Player()
player2 = Player()
player2.penup()
player2.goto(200,200)

while True:
    player1.animate()
    player2.animate()


turtle.mainloop()

'''
turtle.color('blue','red')
turtle.shapesize(8,8,8)
turtle.speed(0)


while True:
    turtle.shape('circle')
    turtle.shapesize(1,1,1)
    time.sleep(.5)
    turtle.shape('circle')
    turtle.shapesize(3,3,3)
    time.sleep(.5)
    
    turtle.shape('circle')
    turtle.shapesize(8,8,8)
    time.sleep(.4)

'''