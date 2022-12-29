def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,20,29,34,23,44,53,55]
print(fun(lst))


def fun(a,b=10):   #b称为默认参数
  print(a,b)

fun(100)
fun(20,30)  
print('hello',end='\t')
print('world')

