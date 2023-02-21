def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in[0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()  #录入学生信息
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()




def menu():
    print('===================学生信息管理系统==================')
    print('---------------------功能菜单---------------')
    print('\t\t\t\t\t\1.录入学生信息')
    print('\t\t\t\t\t\2.查找学生信息')
    print('\t\t\t\t\t\3.删除学生信息')
    print('\t\t\t\t\t\4.修改学生信息')
    print('\t\t\t\t\t\5.排序学生信息')
    print('\t\t\t\t\t\6.统计学生信息')
    print('\t\t\t\t\t\7.显示学生信息')
    print('\t\t\t\t\t\0.退出')
def insert():
    pass
def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__=='__main__':
    main()


