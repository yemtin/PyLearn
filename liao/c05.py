#动态绑定属性
#定义函数
class Student:
    def __init__(self,name,age):  #局部变量
        self.name=name            #实例变量
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

#调用函数
stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)


stu1.eat()
stu2.eat()

#动态方法
def show():
    print('定义在类之外得')
stu1.show=show
stu1.show()
 
