# 文本词频统计 -- Hamlet

def getText():
    txt = open("hamlet.txt","r").read() 
    txt = txt.lower() 
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_’‘“”{|}~`':  
        txt = txt.replace(ch,' ')
    return txt

hamletText=getText()
words = hamletText.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(10):
    print(items[i][0])
