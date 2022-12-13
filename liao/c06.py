#集合之间的关系
#子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,30}
print(s2.issubset(s1))
print(s3.issubset(s2))


#超集
print(s1.issuperset(s2))
print(s2.issuperset(s3))

#交集
print(s2.isdisjoint(s3))