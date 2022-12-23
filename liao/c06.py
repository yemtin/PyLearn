#格式化
#%
name='张三'
age=20
print('我叫%s,今年%d岁' % (name,age))


#{}
print('我叫{0},今年{1}岁'.format(name,age))

print(f'我叫{name},今年{age}')


#精度宽度
print('%10d' % 99) #10表示总宽度
print('%.3f' % 3.1415926)  #3表示小数点后几位
print('%10.3f' % 3.1415926) 

print('{0:.3}' . format(3.1415926))  #一共三位
print('{:.3f}' . format(3.1415926))  #三位小数



