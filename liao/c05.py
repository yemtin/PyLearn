#集合的操作
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,30}
#交集
print(s2.isdisjoint(s3))  
print(s1&s2)

#并集
print(s1.union(s2))
print(s1|s2)
