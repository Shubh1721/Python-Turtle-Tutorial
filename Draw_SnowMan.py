import turtle

pen = turtle.Turtle()
pen.speed(1)
# Title
pen.penup()
pen.goto(-75, 150)
pen.write("Snowman",font=("Times",40))
pen.goto(-75, 120)
pen.write("46 Lines of Code", font=("Times",15))

pen.pensize(5)


# Circle 1
pen.penup()
pen.goto(0,50)
pen.pendown()
pen.color("lightblue")
pen.begin_fill()
pen.circle(30)
pen.end_fill()




# Circle 2
pen.penup()
pen.right(170)
pen.forward(10)
pen.pendown()
pen.color("lightblue")
pen.begin_fill()
pen.circle(45)
pen.end_fill()




# Circle 3
pen.penup()
pen.left(60)
pen.forward(130)
pen.pendown()
pen.color("pink")
pen.begin_fill()
pen.circle(60)
pen.end_fill()


# Buttons
pen.penup()
pen.color("black")
pen.goto(0,30)
pen.dot(20)
pen.goto(0,10)
pen.dot(20)
pen.goto(0,-10)
pen.dot(20)

turtle.mainloop()