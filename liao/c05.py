#元素的获取
#方式1
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三']) 
#print(scores['陈六]) #keyerror
  

#方式2
print(scores.get('张三'))
print(scores.get('陈六'))   #none
print(scores.get('马奇',99))
