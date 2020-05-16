# 货币转换 I 
money = input()
if money[0:3] == 'USD':
    RMB = eval(money[3:]) * 6.78
    print("RMB{:.2f}".format(RMB))
elif money[0:3] == 'RMB':
    USD = eval(money[3:]) / 6.78
    print("USD{:.2f}".format(USD))
