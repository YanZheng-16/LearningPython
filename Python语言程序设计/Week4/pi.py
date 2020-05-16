# 圆周率的计算
import random
num = eval(input())
random.seed(123)
circle = 0
for i in range(1,num+1):
    x,y = random.random(),random.random()
    r = x**2 + y**2
    if r <= 1:
        circle += 1
pi = 4*(circle/num)
print('{:.6f}'.format(pi))
