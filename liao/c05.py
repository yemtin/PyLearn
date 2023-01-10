class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')
class Cat(Animal):
    def eat(self):
       print('猫吃鱼...')

class Person:
    def eat(self):
        print('人吃五谷杂粮')
#定义函数         
def fun(obj):
    obj.eat()
#调用函数
fun(Cat())
fun(Dog())
fun(Animal)

