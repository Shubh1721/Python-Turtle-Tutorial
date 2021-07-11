import turtle

paper = turtle.Screen()
paper.setup(720,720 )   # screen setup krne ke liye
# paper.bgcolor('black') #back-ground color

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)
pen.pencolor("red") 
pen.shapesize(3,3,3)
# pen.goto(-200,5)  
pen.left(90)

# pen.write("Do your HomeWork As soon as possible\nThat's how you will \nlearn codinng", align="left", font=("Comic sans", 16, "bold"))
pen.pencolor('lightblue')

for i in range(0,600,30):
    
    pen.penup()
    pen.setpos(-200,-300+i)
    if i==0:
        pen.right(90)
    pen.pendown()
    pen.forward(400)
    pen.backward(400)

turtle.mainloop()    

# 
