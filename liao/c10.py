
#io操作
'''file=open('a.txt','r')
print(file.readlines())
file.close()
'''

'''file=open('b.txt','w'#代替|'a'追加)
file.write('Python')
file.close()'''


src_file=open('logo.png','rb')

target_file=open('copylogo.png','wb')

target_file.wirte(src_file.read())

target_file.close()
src_file.close()




