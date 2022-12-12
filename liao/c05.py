#集合的相关操作
s={2,3,3,4,5,5,6,7}
#增
s.add(10)  #增一个
print(s)

s.update({200,300,400})  #增几个
print(s)

#删
s.remove(3)  #删一个  指定元素不存在 异常
print(s)

s.discard(6)  #删一个 不存在 不异常
print(s)

s.pop()    #删任意一个 不知道删哪个 不能指定
print(s)

s.clear()
print(s)









