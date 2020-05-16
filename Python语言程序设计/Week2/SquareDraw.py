# turtle正方形绘制
import turtle
turtle.setup(600, 600, 0, 0)

turtle.pensize(10)      
turtle.pencolor("black")
for i in range(4):
    turtle.fd(150)
    turtle.left(90)

turtle.done()
