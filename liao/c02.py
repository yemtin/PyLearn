
#continue
'''要求输出1-50之间所有5的倍数'''
for item in range(1,51):
    if item%5==0:
        print(item)


        print('------------使用continue-----------')
        for item in range(1,51):
            if item%5!=0:
                continue
            print(item)

