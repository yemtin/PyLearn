#列表
a=10  #变量存储的是一个对象的引用
#获取列表中的单个元素
lst=['hello','world',98,'hello','world',234]
print(lst[2])
print(lst[-3])





def list_operation():
    #获取列表中多个元素  列表名[start:stop:step]
    lst=[10,20,30,40,50,60,70,80]
    #print(lst[1:6:1])
    print('原列表',id(lst))
    lst2=lst[1:6:1]     #切出来的组成新的列表
    print('切的片段',id(lst2))
    print(lst[1:6])
    print(lst[1:6:])
    print(lst[::-1])  #倒着


# list_operation()


def list_cut():
    pass

#判断元素是否在列表 in     not in
lst=[10,20,30,'Python']
print(10 in lst)
print(100 in lst)
print('-------------------------------------')
for item in lst:
    print(item)


def type_hint(a: int) -> int:
    c = a.bit_length()
    print('---', c)

    return c





if __name__ == "__main__":

    # list_operation()
    # list_cut()
    b = type_hint(759)

    s: str