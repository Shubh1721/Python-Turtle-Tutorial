import turtle
import time

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('ShubhGurukul-PauseDemo')
player = turtle.Turtle()
player.shape('triangle')
player.shapesize(3,3)
player.color('yellow')
player.penup()

is_clicked = False

def toggle():
    global is_clicked
    if is_clicked == False:
        is_clicked = True
    else:
        is_clicked = False

is_red = False
def redToggle():
    global is_red
    if is_red == False:
        is_red = True
        player.color('red')
    else:
        is_red = False
        player.color('yellow')

wn.listen()
wn.onkeypress(toggle, 'p')
wn.onkeypress(redToggle, 'r')

startTime =time.time()
timeLimit = 5
print(startTime)
while True:
    if not is_clicked:
        player.forward(1)
        player.left(1)
        elapsed_time = time.time()-startTime
        
        print(timeLimit - int(elapsed_time))
        if(timeLimit - int(elapsed_time))<0:
            exit()

    else:
        wn.update()    

turtle.mainloop()
