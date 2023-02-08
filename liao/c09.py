'''def add(a,b):
    return a+b
def div(a,b):
    return a|b


#如何导入自定义模块




#c09.py中导入calc自定义模块使用
import calc
print(calc.add(10,20))
from calc import add
print(10,20)'''




'''def add(a,b):
    return a+b


print(add(10,20))


if __name__=='__main__':
    print(add(10,20))  #只有当点击运行c10.py时，才会执行'''


'''import c10
print(c10.add(100,200))'''




'''import sys
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))'''





'''#第三方模块安装及使用
#每间隔多长时间执行一次操作任务
import schedule
import time


def job():
    print('哈哈----------------')

schedule.every(3).seconds.do(job)  #三秒执行一次
while True:
    schedule.run_pending()
    time.sleep(1)  #执行一次休眠一秒'''








