def fun(*A):  #可变的位置形参  结果为元组
    print(A)

fun(10)
fun(10,20,30)
fun(38,49,59,60)


def fun(**B):
    print(B)
fun(a=20)
fun(a=10,b=30,c=40)


