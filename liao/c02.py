
a=0
while a<3:  #条件执行体
    pwd=input("请输入密码：")
    if pwd=="8888":
     print("密码正确")
     break
    else:
       print("密码不正确")
       a+=1    #改变变量