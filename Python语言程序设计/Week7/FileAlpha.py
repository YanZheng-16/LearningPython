# 文件行数
f = open("latex.log",'r',encoding='utf-8').read()
alpha = 'abcdefghijklmnopqrstuvwxyz'
counts = {}
s = 0
for a in f:
    s += 1
    if a in alpha:
        counts[a] = counts.get(a,0) + 1
        
m = 0
print('共{}字符'.format(s), end = '')
for i in range(26):
    print(',{}:{}'.format(alpha[i],counts[alpha[i]]), end = '')
    m += counts[alpha[i]]

'''
题中要求的“一共包含的字符数量”，指包括特殊符号、小写字母等等在内的全部字符数
'''
