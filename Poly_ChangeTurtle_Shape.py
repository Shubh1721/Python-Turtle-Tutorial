import turtle

turtle.pensize(7)

turtle.begin_poly()
for i in range(5):
    turtle.forward(100)
    turtle.left(144)

turtle.end_poly()

star = turtle.get_poly()
print(star)

turtle.register_shape("star",star)

turtle.shape("star")
turtle.forward(300)
for i in range(5):
    turtle.forward(200)
    turtle.left(144)





turtle.mainloop()