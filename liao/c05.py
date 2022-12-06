#remove
lst=[10,20,30,50,60,70]
lst.remove(30)
print(lst)

#pot
lst.pop(1) #根据索引移除 如果不写索引，删最后一个
print(lst)

print('----------------切片，删除至少一个元素，产生新列表-------------------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)
#不产生新列表
lst[1:3]=[]
print(lst)

#清除所有
lst.clear()
print(lst)

#删除列表
del lst
print(lst)
