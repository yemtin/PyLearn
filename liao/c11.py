'''book_name='java程序设计教程'
publish='西安电子科技大学出版社'
pub_date='2019-02-02'
price=56.8
print('►➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛◄')
print('▷\t\t《',book_name,'》\t\t ◁')
print('▷\t\t出版社:',publish,'\t◁')
print('▷\t\t出版时间:',pub_date,'\t\t◁')
print('▷\t:定价:',price,'\t\t\t\t◁')
print('►➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛➛◄')'''





'''lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['➊','➋','➌','➍','➎']
for i in range(5):
    print(lst_name[i],lst_sig[i])

d={'➊':'林黛玉','➋':'薛宝钗','➌':'贾元春','➍':'贾探春','➎':'史湘云'}
print('------------------------------------------------------')
for key in d:
    print(key,d[key])


print('zip-------------------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)'''







'''num=int(input('请输入一个十进制的整数'))
print(num,'的二进制为：',bin(num))
print(str(num)+'的二进制数为'+bin(num))
print('%s的二进制数为:%s' % (num,bin(num))) #格式化
print('{0}的二进制为:{1}'.format(num,bin(num)))
print(f'{num}的二进制为：{bin(num)}')   #print('{num}的二进制为：{bin(num)}')则输入一行字符串'''


'''print('当前余额为：\033[0;35m8元\033[m')
money=int(input('请输入充值金额：'))
money+=8
print('当前余额为：\033[0.32m',money,'元\033[m')
'''



'''def get_number(s,ch):
    number=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            number+=1
    return number
    if_name_=='_main_'
s='hello,i am origenally from zhanjiang'
ch=input('请输入字符')
number=get_number(s,ch)
print(f'{ch}在{s}中出现的次数为:{number}')
'''



'''s=input('请输入密码')
if s.isdigit():
    print('输入数字合法')
else:
    print('输入数字不合法')
print('-----------------------------------')
print('输入数字合法'if s.isdigit() else '输入数字不合法')'''


'''count=input('请输入qq号')
password=input('请输入密码')
if count=='123456' and password=='654321':  #字符串别忘记用引号
    print('登录成功')
else:
 print('登录失败')'''


'''import random
price=random.randint(1000,1500)
print('今日竞猜商品价格为小米扫地机器人:价格在[1000,1500]之间:')
guess=int(input())
if guess>price:
    print('大了')
elif guess<price:
    print('小了')
else:
    print('猜对了')
print('商品真实价格为：',price)'''







'''x=97
for _ in range(1,27):
 print(chr(x),'--------->',x)
 x+=1

 print('-----------------------------')
x=97
while x<=123:
    print(chr(x),'------>',x)
    x+=1
'''


'''for z in range(1,4):
 x=input('请输入用户名')
 y=input('请输入密码')
 if x=='adfmin' and y=='adm':
    print('登录成功')
    break
 else:
    print('用户名或密码不正确')
    if z<3:
     print('您还有',3-z,'次机会')
else:                                 #否则循环结束！！！！！！
    print('对不起，三次均错误，请联系后台人员')'''


'''import random
ran=random.randint(1,100)
for i in range(1,11):
    num=int(input('在我心中有个数，请你猜一猜'))  #记得输入的是整数形式!!!!!!
    if num<=ran:
        print('小了')
    elif num>=ran:
        print('大了')
    else:
        print('才对了！！！！')
        break
print('您一共猜了',i,'次')
if i<=3:
    print('你真聪明！')
elif i>3 and i<=7:
    print('还行吧')
else:
    print('你真笨！')'''





        

'''coffee_name=('Blue Mountain','cappuccino','latte','royal coffee','queen coffee','beauty and sorrow')
print('hello,welcome to yemtin’s coffeehouse')
print('here is our coffee list：')
for index,item in enumerate(coffee_name):
    print(index+1,'.',item,end='')   #index begin by 0 end='' intended to not change the line

index=int(input('\nplease input your coffee’s number:'))
if 0<=index<=len(coffee_name):
    print(f'here is your coffee[{coffee_name[index-1]}],enjoy yourself')'''


try:
 score=int(input('please input ypur score:'))  
 if 0<=score<=100:
    print('your score is:',score)
 else:
    raise Exception('number is wrong')
except Exception as e:
    print(e)






