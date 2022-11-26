#pratice:要求输出100-999之间的水仙花数(eg:153=3*3*3+5*5*5+1*1*1)
for item in range(100,1000):
               ge=item%10
               shi=item//10%10
               bai=item//100
               print(ge,shi,bai)