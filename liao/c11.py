fp=open('d:/liao','w')
print('奋斗成就更好的你',file=fp)
fp.close


with open('d:/liao','w') as file:
    file.write('奋斗成就更好的自己')