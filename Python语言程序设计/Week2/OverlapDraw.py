# turtle叠边形绘制
import turtle
turtle.setup(600, 600, 0, 0)
turtle.pensize(10)
turtle.penup()
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.pendown()
for i in range(9):
    turtle.fd(150)
    turtle.left(80)

turtle.done()
