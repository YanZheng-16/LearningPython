# turtle六边形绘制
import turtle
turtle.setup(600, 600, 0, 0)

turtle.pensize(10)      
turtle.pencolor("black")
for i in range(6):
    turtle.fd(100)
    turtle.left(60)

turtle.done()
