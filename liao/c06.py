#向列表末尾添加一个元素
lst=[10,20,30]
lst.append(100)
print(lst)

#extend
lst=[10,20,30,40]
lst2=[80,90]
lst.extend(lst2)
print(lst)


#insert
lst=[19,29,39,49]
lst.insert(1,90)
print(lst)


#切片
lst3=[True,False,'hello']
#在任意位置添加n多个元素
lst[1:]=lst3
print(lst)