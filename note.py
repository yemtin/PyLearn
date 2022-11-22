# 内存 二进制  bit byte

# 0101011100
# bit 位  这个位就是平常说个位十位百位的那个位
 # 十进制 的话 一位就有 10 种可能 0， 1， 2，3， 。。。， 9
 # 二进制 的话 一位只有 2种可能 即 0 和 
 # 8位 为一个字节byte 既可以表示英文世界的各种符号 所以以8位为一个单位。00001111 
 # 00000000  表示数字 0 ， 00000001 表示数字ASCII 码  00

# 硬盘(512GB) 到 内存（16GB）byte 字节    ByteDance 字节跳动 GB 代表字节 Gb 代表位


# 变量

a = 10
name = 'mtin'

# 三种基本结构/语句
# 1. 顺序结构
# 2. 条件结构
# 3. 循环结构

if a > 8:  # True
    print(name)

if a > 15:  # False
    print('我大于15哦')
else:
    print('谁说我比15大')

# for  while

for item in name: # for ... in ...
    print(item)

index = 0

while a > 3 :
    # index = index +1
    index += 1
    print(index, a)
    a = a -1

else:
    print('我over了')
# if .... for ...



# 函数  （抽象）
# 数学中的函数 y = f(x) : y = 3x +2
def f(x):
    # block
    y = 3*x + 2
    return y
    print('不要我了吗 ')

result = f(6)
print(result)

def loop_name():
    zz = 2
    for item in name: # for ... in ...
        print(item)


loop_name()

loop_name()

loop_name
# 面向过程

# 类 Object oriented 面向对象  台湾： 物体导向  我: 物化
class Person():

    def __init__(self, name, age, length, gender='女'):
         self.name = name
         self.age = age
         self.length = length
         self.gender = gender

    def run(self):
        print('我跑得帅不帅~')
    
    def read(self):
        print('我认不认真？')

me = Person(name='mtin', age=18, length=168)  # 实例化
xiaohua = Person('xiaohua', 22, 188, gender='男')

me.run()
me.read()

print(xiaohua.name, xiaohua.length)
# namespace 命名空间 module 模块 包


