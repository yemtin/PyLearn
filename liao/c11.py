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



def get_count(s,ch):
    count=0
    for item in s:
        if ch.upper()==item or ch.lower()==item:
            count+=1
            return count
            if_name_=='_main_'
s='hello,i am origenally from zhanjiang'
ch=input('请输入字符')
count=get_count(s,ch)
print(f'{ch}在{s}中出现的次数为:{count}')









