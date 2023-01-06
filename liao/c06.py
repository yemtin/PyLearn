 #封装
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')
car=Car('宝马')
car.start()
print(car.brand)


class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类外部被使用，加__
    def show(self):
        print(self.name,self.__age)
stu=Student('张三',20)
stu.show()
#在类外面使用age
#print(stu.__age)  #错误
#print(dir(stu))  #查询怎么使用
print(stu._Student__age)
