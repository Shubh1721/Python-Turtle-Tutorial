import turtle as pen
pen.penup()
pen.goto(30,170)
pen.pendown()
# Background Pic
pen.bgpic("3.gif")
pen.setup(500,500)

pen.speed(0)
# Outer Anime
pen.pensize(10)
pen.pencolor("black")
pen.fillcolor("purple")

pen.begin_fill()

pen.goto(80,130)
pen.goto(100,80)
pen.goto(80,30)
pen.goto(100,-10)
pen.goto(120,70)
pen.goto(130,40)
pen.goto(160,60)
pen.goto(140,0)
pen.goto(120,-80)
pen.goto(130,-150)
pen.goto(-100,-150)
pen.goto(-80,-100)
pen.goto(-120,-40)
pen.goto(-150,-30)
pen.goto(-160,0)
pen.goto(-120,0)
pen.goto(-130,20)
pen.goto(-80,-50)
pen.goto(-80,-10)
pen.goto(-110,20)
pen.goto(-100,100)
pen.goto(-60,170)
pen.goto(30,170)

pen.end_fill()

# Left Eye
pen.penup()
pen.goto(-40,100)
pen.pendown()

pen.pensize(2)
pen.fillcolor("white")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

#right Eye
pen.penup()
pen.goto(30,100)
pen.pendown()

pen.pensize(2)
pen.fillcolor("white")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Star
pen.penup()
pen.goto(130,60)
pen.pendown()

pen.pensize(8)
pen.pencolor("gold")
pen.fillcolor("gold")
pen.begin_fill()
pen.goto(150,90)
pen.goto(160,60)
pen.goto(180,60)
pen.goto(160,40)
pen.goto(170,20)
pen.goto(140,40)
pen.goto(110,20)
pen.goto(130,40)
pen.goto(110,60)
pen.goto(130,60)
pen.end_fill()


pen.penup()
pen.goto(-50,70)
pen.pendown()

pen.pensize(8)
pen.pencolor("white")
pen.fillcolor("red")
pen.begin_fill()
pen.goto(50,70)
pen.goto(30,30)
pen.goto(-30,30)
pen.goto(-50,70)
pen.end_fill()


# Title
pen.penup()
pen.color("Yellow")
pen.goto(-40,-195)
pen.write("Barney",font=("Arial",30,"bold"))
pen.goto(-40, -215)
pen.write("100 Lines of Code",font=("Times", 20))


# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))

pen.mainloop()



