# 《沉默的羔羊》之最多单词
import jieba

f = open('沉默的羔羊.txt', 'r', encoding='utf-8').read()
words = jieba.lcut(f)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word]=counts.get(word,0) + 1

list = list(counts.items())
list.sort(key=lambda x:x[1],reverse=True)
print(list[0][0])
