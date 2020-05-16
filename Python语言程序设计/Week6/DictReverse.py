# 字典翻转输出
d1 = eval(input())

try:
    d2 = dict(zip(d1.values(), d1.keys()))
    print(d2)
except:
    print("输入错误")
