s='hello,python'
print(s.replace('python','Java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))  #替换前两个


print('|'.join(s))
print('*'.join(s))


print('apple'>'app')
print('apple'>'banana')  #比较原始值
print(ord('a'),ord('b'))  #得到原始值
print(chr(97),chr(98))    #得到原来的字符
print(ord('p'),ord('a'))
