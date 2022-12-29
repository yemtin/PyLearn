#变量
def fun(a,b):
    c=a+b   #c为局部变量
    print(c)

name='ye'  #name为全局变量
print(name)
def fun2():
    print(name)
fun2()


