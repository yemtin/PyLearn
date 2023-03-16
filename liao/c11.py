



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





lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['➊','➋','➌','➍','➎']
for i in range(5):
    print(lst_name[i],lst_sig[i])

d={'➊':'林黛玉','➋':'薛宝钗','➌':'贾元春','➍':'贾探春','➎':'史湘云'}
print('------------------------------------------------------')
for key in d:
    print(key,d[key])


print('zip-------------------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)



