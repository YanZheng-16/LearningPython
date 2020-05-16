# 任意累积
def cmul(*s):
# 在参数名前面的*表示s是一个可变参数
    result = 1
    for i in s:
        result *= i
    return result

print(eval("cmul({})".format(input())))
