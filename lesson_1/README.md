Lesson 1  附加题
===============================
#### My Blog：[灵柩里的人][1]

 [1]: http:www.coffin5257.com

**一、python中有几种注释，分别是干什么用的**
```python
#注释单行
/*
 *注释代码块
 */
```
**二、说出变量的定义法则并写一个变量**
开头仅以 _ 或 字母(包括大小写)，变量名大小写敏感。

**三、判断下面的语句是否正确如果正确请写出答案，如果错误请改正后写出运算结果**
```python
(1)
$a=123
print $a
#error 变量名去掉$ 输出123
(2)
c='123+ABC'
print c
#correct 输出123+ABC
(3)
b='A'+'B'
print b
#correct 输出AB
(4)
A='123+456'
print a
#error 两个变量名统一 输出123+456
(5)
B=true+1
print B
#error:name 'true' is not defined
#To correct:true得是个int/float型的变量 或者 改成True
(6)
a=1
if(a=1){
print '正确'
}else{
print '错误'
}
#To correct:
#--------------------
#coding=utf-8
a=1
if(a==1):
    print '正确'
else:
    print '错误'
#---------------------
输出正确
(7)
a=5
if a != 7 :
    a+=1
print a
#输出6
(8)
A=（1，2，3，4，5）
A.append('6')
print A
#error 元组没有append 把()换成[]
#输出[1, 2, 3, 4, 5, '6']
(9)
a='ABC'
a[2]='B'
#error

a='1'
b=2
a+b=？
#应该怎么运算？
#无法直接运算，需要更改其中一个变量类型

a='1'
b='2'
a+b=？
#Result:'12'
```
**四、请写出如何判断'AB123542132547231'这段字符串里有多少个'1'存在，判断7的位置
判断开头是否是AB并说出返回的是一个什么值(数据类型)，该数据类型的值(数值)为多少**
```python
#coding:utf-8
a='AB123542132547231'
print a.count('1')
print a.find('7')
print a.startswith('AB')
print type(a.startswith('AB'))
```
**五：请把该字符串转换为列表 '我爱暗影'**
```python
#!/usr/bin/env python
#coding:utf-8
a=u'我爱暗影'
a=a.replace('',' ')
a=a.strip()
print a
b=a.split(' ')
print b
```

**六：请把该字符串变为大写 'abcdef'**
```python
#!/usr/bin/env python
a='abcdef'
b = a.upper()
print b
```

**七:定义一个值含A的列表
(1)向里面添加一个值
(2)删除最后一个值
(4)删除值为A
(5)删除第二个值
(6)循环此列表分别打出此列表的索引和值**
```python
#!/usr/bin/env python
alist = ['1','a','A','b','2']
print alist
alist.append('c')
print alist
alist.pop()
print alist
alist.remove('A')
print alist
del alist[1]
print alist
x = 0
for a in alist:
	print 'index:%d\tvalue:%s' % (x,a)
	x+=1
```

**八：用2种方法写出a=[1,2,3,4,5]的倒序**
```python
a.reverse()
a[::-1]
```
(1)a[-3]的值是多少
```python
3
```
(2)用切片取出234的值
```python
a[1:4]
```
(3)a[1:5:2]的值是多少1,5,2分别是什么
```python
[2,4] a[x:y:z] 输出x、y之间的元素，间隔z
``` 
(4)a = 'abcd' 用2个方法取出字母d
```python
a[len(a)-1]
a[-1]
```
**九:运行下面结果并分析**
```python
(1)
a=['a','b','c','d','e'] 
for x in range(len(a)): #从 0到len(a)-1，即0 1 2 3 4
    print x
#Reult:
0
1
2
3
4
(2)
a=1
while 1:
    a+=1
    if a==3 #need : here
        break
    print a
To correct Result:
2
(3)
bool("521" == 521)的结果是什么
False

此循环正确吗 为什么?
a=1
while a:
    print 1
#Error 无限循环 a永远为真
```
**十:分析下列结果**
```python
a=[1,2,3,4,5,6,7,8,9,10]
for x in a: #从前到后遍历
    print a.pop() #弹出最后一个应返回该值
    if x==4:
        print '我爱暗影'
#Result
10
9
8
7
我爱暗影
6
```
