# 三位水仙花数
s = []
a = ','
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            num1 = i*100 + j*10 + k
            num2 = i**3 + j**3 + k**3
            if num1 == num2:
                s.append(str(num1))
print(a.join(s))
