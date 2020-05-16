# CSV格式数据清洗
f = open("data.csv")
for line in f:
    line = line.strip("\n")
    line = line.replace(" ", "")
    line = line.split(",")
    print(",".join(line))
f.close()
