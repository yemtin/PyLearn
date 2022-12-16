#字符串大小写的转换
s='hello,python'
a=s.upper()  #转大
print(a)
b=s.lower() #转小
print(b)
c=s.swapcase() #小->大 大->小
print(c)
d=s.capitalize() #all the first
print(d)
f=s.title()  #each first 
print(f)



#对齐
s="hello,Python"
print(s.center(20,'*'))  #居中对齐

print(s.ljust(20,"*"))  #左对齐
print(s.ljust(10))
print(s.ljust(20)) 

print(s.rjust(20,'*'))  #右对齐

print(s.zfill(20))  #zero fill
print(s.zfill(10))  #小于 返回元字符
print('-8910'.zfill(8))


#劈分
s='hello world Python'
print(s.split())
lst=s.split()
print(lst)
s1='hello|world|Python'
print(s1.split(sep='|'))  #sep指定劈分符
print(s1.split(sep='|',maxsplit=1))  #规定最大劈分

