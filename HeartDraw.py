import turtle
# Creating turtle
pen = turtle.Turtle() # pen bnaya
paper = turtle.Screen() # paper bnaya
paper.bgcolor("black")  # paper ka color black kra
pen.pensize(5)
# To design curve
pen.shape("turtle")
pen.speed(3)   # pen ki speed 3 ki jisse dikhe ske ki pen kaise move kiya

pen.color("red", "pink")    #  phla color likhne ke liye aur dusra color fill krne ke liye 
pen.shapesize(6,6,6)

pen.begin_fill()

pen.left(140)
pen.forward(111.65)

# phla curve
for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.left(120)

# Doosra Curve
for i in range(200):
    pen.right(1)
    pen.forward(1)

pen.forward(111.65)
pen.end_fill()

# pen.hideturtle()    # pen ko chhipaya(hide) kiya

turtle.mainloop()

