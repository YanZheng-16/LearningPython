# 天天向上的力量
def WeekUp(dp):
    dayUp = 1.0;
    for i in range(365):
        if i%7 in [6, 0]:
            dayUp *= (1 - 0.01);
        else:
            dayUp *= (1 + dp);
    return dayUp; 

A = pow(1.01, 365)
 
dayUpp = 0.01;
while WeekUp(dayUpp) < A:
     dayUpp += 0.001;
 
print("工作日的努力参数是: {0:.3f}".format(dayUpp))
