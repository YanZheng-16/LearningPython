# 身体质量指数BMI
height, weight = eval(input())
BMI = weight/height**2
print("BMI数值为:{:.2f}".format(BMI))
if BMI < 18.5:
    print("BMI指标为:国际'偏瘦', 国内'偏瘦'")
elif BMI > 18.5 and BMI <24:
    print("BMI指标为:国际'正常', 国内'正常'")
elif BMI > 24 and BMI <25:
    print("BMI指标为:国际'正常', 国内'偏胖'")
elif BMI > 25 and BMI <28:
    print("BMI指标为:国际'偏胖', 国内'偏胖'")
elif BMI >= 28 and BMI <30:
    print("BMI指标为:国际'偏胖', 国内'肥胖'")
elif BMI >= 30:
    print("BMI指标为:国际'肥胖', 国内'肥胖'")
    
'''
代码的两点问题：
1、临界取等条件无法判断；
2、无法通过测试用例，可能是中文部分和答案有偏差
'''
