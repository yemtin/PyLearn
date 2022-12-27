#编码和解码
s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #在GBK这种编码格中一个中文占两个字节
print(s.encode(encoding='UTF-8'))  #占三格

bytes=s.encode(encoding='GBK')  #编码
print(bytes.decode(encoding='GBK')) #解码
bytes=s.encode(encoding='UTF-8')
print(bytes.decode(encoding='UTF-8'))


