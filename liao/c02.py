#列表
a=10  #变量存储的是一个对象的引用
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)


#创建列表的第一种方式，[]
lst=['hello','world',98]

'''第二种,内置函数list()'''

lst2=list(['hello','world',98])




#获取指定元素的索引
lst=['hello','world',98,'hello']
print(lst.index('hello')) #如果列表中有相同元素，只返回第一个
#print(lst,index('Python')) #error:'Python' id not in lst
print(lst.index('hello',1,3))  #后面为指定范围



#获取列表中单个元素
print(lst[2])
