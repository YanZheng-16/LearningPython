#Python蟒蛇绘制
import turtle

#setup设置窗体大小及位置（宽， 高， 左上角点x, 左上角点y）
turtle.setup(1920, 1080, 0, 0)

turtle.penup()          #抬起画笔（海龟）
turtle.fd(-250)         #海龟倒退250个像素
turtle.pendown()        #放下画笔（海龟）
turtle.pensize(25)      
turtle.pencolor("purple")   #画笔颜色
turtle.seth(-40)        #海龟方向为-40度方向（直角坐标内）
for i in range(4):      #for下的语句循环4次
    turtle.circle(40, 80)      #海龟走曲线（半径，弧度）
    turtle.circle(-40, 80)     
turtle.circle(40, 80/2)        #绘制小半个弧形
turtle.fd(40)               #向海龟方向前进40像素，构成蟒蛇脖子
turtle.circle(16, 180)       
turtle.fd(40 * 2/3)          #半圆形和直线构成蟒蛇头部   
turtle.done()               #绘制完毕后程序需手动退出
