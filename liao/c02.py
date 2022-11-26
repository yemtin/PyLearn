#for-in 循环
for item in "python":   #将phthon里的值一次付给item
    print(item)


    for i  in range(10):
        print(i)


    for _ in range(5):
      print("人生苦短,我用python")

      #使用for循环计算1-100之间的偶数和
      sum=0   #用于存储偶数和
      for item in range(1,101):
         if item%2==0:
            sum+=item
            print('1-100之间的偶数和为:',sum)


            #pratice:要求输出100-999之间的水仙花数(eg:153=3*3*3+5*5*5+1*1*1)
            for item in range(100,1000):
               ge=item%10
               shi=item//10%10
               bai=item//100
               print(ge,shi,bai)

     