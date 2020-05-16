# 凯撒密码
password = input()
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
before = A.lower() + A
after = B.lower() +B

for i in password:
    if i in before:
        rank = before.index(i)
        print(after[rank], end="")
    else:
        print(i, end="")
