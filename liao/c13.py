def getText():
    txt=open("D:\code\PyLearn\liao\哈利波特1-7英文原版.txt",'r').read()
    txt.lower()
    for ch in "!@#$%""^&*(){}_+:<>?~'',.":
        txt=txt.replace(ch,' ')
    return txt
harrypoterText=getText()
words=harrypoterText.split()
counts={}  #字典
for word in words:
    counts[word]=counts.get(word,0)+1  #
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10000):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))
 