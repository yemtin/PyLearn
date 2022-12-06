#排序
lst=[20,40,10,98,54]
print('排序前的',lst)
lst.sort()    #升序
print('排序后的',lst)

lst.sort(reverse=True)  #降序  reverse=False 为升序
print(lst)


print('---------------------使用内置函数sorted(),产生新的列表---------------------')
lst=[20,40,10,98,54]
print('原列表',lst)
new_list=sorted(lst)
print(lst)
print(new_list)



