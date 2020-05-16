# 文件独特行数
f = open("latex.log")
row = f.readlines()
r1 = set(row)
for i in r1:
    row.remove(i)
r2 = set(row)

print("共{}独特行".format(len(r1)-len(r2)))
