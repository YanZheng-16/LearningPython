# 文件行数

f = open("latex.log",'r',encoding='utf-8')
row = 0
for line in f:
    line = line.strip('\n')
    if len(line) != 0:
        row += 1
print("共{}行".format(row))
