class Studend:
    #pass
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return'我得名字是{0}，今年{1}岁'.format(self.name,self.age)
stu=Studend('张三',20)
print(dir(stu))
print(stu)
print(type(stu))
                                                                                                                                                                           

