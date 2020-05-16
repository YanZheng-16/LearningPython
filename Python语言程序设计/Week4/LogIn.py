# 用户登录的三次机会
for i in range(3):
    name = input()
    password = input()
    if name == 'Kate' and password == '666666':
        print('登录成功！')
        break
    if i == 2:
        print('3次用户名或者密码均有误！退出程序。')
