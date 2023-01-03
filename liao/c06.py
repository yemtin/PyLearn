class Student:   #类的名称 由一个单词或多个单词 首字母大写
    native_pace='吉林'
    #初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def eat(self):
        print('学生吃饭...')
    #静态方法
    @staticmethod
    def method():
        print('静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('类方法')

#在类之外叫函数
def drink():
    print('喝水')

#创建student类对象
stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)
print('-------------------------------------------')
print(id(Student))
print(type(Student))
print(Student)
print('-----------------------------------------------------')
stu1.eat()
print(stu1.age)
print(stu1.name)
print('--------------------------------')
Student.eat(stu1)

#类属性的使用方法
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
