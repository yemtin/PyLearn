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