'''流程控制语句在二重循环中的使用'''
for i in range(5):   #外层执行5次 i=0
    for j in range(1,11):  #j=1
        if j%2==0:
            break
        print(j)




for i in range(5):
    for j in range (1,11):
        if j%2==0:
            break
    print(j)


for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')   #不换行，在末尾加空格
    print()  #换行


for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
    print(j,end='\t')


        
                


