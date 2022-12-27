def calc(a,b):  #a,b称为形势参数，简称形参
    c=a+b
    return(c)

result=calc(10,20)  #10，20称为实参
print(result)

res=calc(b=10,a=20)
print(res)