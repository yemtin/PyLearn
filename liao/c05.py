#继承
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age,stu_no):
        super().__init__(name, age)
        self.stu_no=stu_no
    def info(self): 
        print(self.stu_no)  

class Teacher(Person):
    def __init__(self, name, age,teachofyear):
        super().__init__(name, age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)

stu.info()
Teacher.info()

