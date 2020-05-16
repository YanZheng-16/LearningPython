# 数字形式转换 I
num = input()
a = '0123456789'
A = '零一二三四五六七八九'
for i in num:
    rank = a.index(i)
    print(A[rank], end="")
