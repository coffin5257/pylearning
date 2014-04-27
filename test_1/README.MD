1、列表中的 remove 函数,接收的参数是值还是索引?
**值**

2、用 python 的向他深深道歉(控制台输出”对不起,我错了”)
```print '对不起，我错了'```

3、计算 1 到 50 的和,并筛选出其中的奇数
```python
s = 0
for x in range(1,50):
	s+=x
	if x%2 == 1:
		print x
print s
```

4、5 个数字,依次用列表添加整形 90,33,字符串“45”,“21”,浮点型 15.5,降序输出,然后将字符串强制转换为整形,并用 for 循环(或者 while)计算总和
```python
alist = []
alist.append(90)
alist.append(33)
alist.append('45')
alist.append('21')
alist.append(15.5)
alist.sort()
alist.reverse()
print alist
s = 0
for x in alist:
	if type(x)==type('a'):
		x = int(x)
	s += x
print s
```

5、一个字典{'name':'huahua','age':31}。首先判断 age 是否存在字典中,如果存
在,再次判断是否大于 30,如果大于 30 修改 age 的 值为 29。
```python
adict = {'name':'huahua','age':31}
if 'age' in adict:
	if adict['age']>30:
		adict['age'] = 29
print adict
```

6、'abcdefaigcdtewscs'这串字符串中’c’共出现了几次?并输出索引为 3 到 9 (包含9)的子字符串。
```python
str = 'abcdefaigcdtewscs'
print str.count('c')
print str[3:10]
```

7、改错：
程序一：
添加元素要用 add 方法 s.add(88)
集合没有find方法 可以用 78 in s
程序二：
比较应该用 ==

8、{‘a’:54,’b’:38,’c’:79,’d’:84} 判断 value 是否大于 63,如果大于,则删除。并输出删除之后的字典。
```python
adict = {'a':54,'b':38,'c':79,'d':84}
for x in adict.keys():
	if adict[x] > 63:
		del adict[x]
print adict
```

9、集合
```python
me = set(['orange','strawberry','mango'])
niangpao = set(['apple','orange','strawberry'])
print me&niangpao
```

10、Dotxyoutxthink,youtxwintxthistxexam?
```python
a='Dotxyoutxthink,youtxwintxthistxexam?'
a.replace('tx',' ')

'Do you think,you win this exam?'
```

11、下面是一串数据
name|age|time|id|tel
:||||
zhangsan|11|2011-4-20 20:20:21|000001|12345678901
lisi|28|2011-4-20 21:00:51|000002|34567890120
guangtouqiang|33|2011-4-20 21:10:43|000003|12309876512
shezhang|29|2011-4-20 21:11:15|000004|99999999999
dream9|15|2011-4-20 21:14:04|000005|21522131328
请复制到你的变量中,然后找出它们的规律,如花说他只要 name,age,tel 这三个信息,让我们从这里面筛选出来。
```python
a = {'name':'zhangsan','age':'11','time':'2011-4-20 20:20:21','id':'000001','tel':'12345678901'}
b = {'name':'lisi','age':'28','time':'2011-4-20 21:00:51','id':'000002','tel':'34567890120'}
c = {'name':'guangtouqiang','age':'33','time':'2011-4-20 21:10:43','id':'000003','tel':'12309876512'}
d = {'name':'shezhang','age':'29','time':'2011-4-20 21:11:15','id':'000004','tel':'99999999999'}
e = {'name':'dream9','age':'15','time':'2011-4-20 21:14:04','id':'000005','tel':'21522131328'}

info = [a,b,c,d,e]
for x in info:
	del x['time']
	del x['id']
	print x
```

12、请将下面的['a',1,88,31,'time',66,'year','deep',33,(3,2,4),['a','b','c'],12,'小芝麻98',{},'1','woca','15','写不下去了',"study",'2014-2-24 19:58:33',"",3,6,9,'ai','yumen',3,'7',8,12,2]进行判断是否为数值,如果是数值而且不重复则存入一个新的容器,然后进行正向排序,最后相加所有的数值和
```python
#encoding:utf-8
a = ['a',1,88,31,'time',66,'year','deep',33,(3,2,4),['a','b','c'],12,u'小芝麻98',{},'1','woca','15',u'写不下去了',"study",'2014-2-24 19:58:33',"",3,6,9,'ai','yumen',3,'7',8,12,2]
tmp = []
for x in a:
	if type(x) == int:
		tmp.append(x)
tmp.sort()
print tmp
s = 0
for x in tmp:
	s+=x
print s
```