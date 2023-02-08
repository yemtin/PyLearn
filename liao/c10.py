
#io操作
'''file=open('a.txt','r')
print(file.readlines())
file.close()
'''

'''file=open('b.txt','w'#代替|'a'追加)
file.write('Python')
file.close()'''


src_file=open('logo.png','r',encoding='UTF-8')

target_file=open('copylogo.png','w',encoding='UTF-8')

target_file.wirte(src_file.read())

target_file.close()
src_file.close()

#FileNotFoundError: [Errno 2] No such file or directory: 'logo.png'


file=open('a.txt,'r'')
print(file.read(2))












