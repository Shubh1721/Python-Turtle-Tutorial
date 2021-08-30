import turtle

turtle.shapesize(3,3,3)
turtle.pensize(5)

def mouseClick(x=0,y=0):
	# print(x,y)
	turtle.goto(x,y)


turtle.listen()

turtle.onscreenclick(mouseClick)


turtle.mainloop()















# import turtle
# import random

# col = ['red', 'yellow', 'green', 'blue',
# 	'white', 'black', 'orange', 'pink']

# def fxn(x, y):
# 	global col
# 	ind = random.randint(0, 7)
# 	sc.bgcolor(col[ind])

# sc = turtle.Screen()
# # sc.setup(400, 300)
# turtle.speed(0)
# # turtle.onscreenclick(fxn)
# # turtle.ondrag
# def fow(x,y):
#     turtle.goto(x,y)
# # turtle.listen()
# # turtle.onclick(fow)    
# turtle.ondrag(fow)

# turtle.mainloop()