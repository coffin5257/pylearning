My Blog ：[灵柩里的人][1]
==================================
##第一题：python中有几种注释方法
```python
print 'http://www.coffin5257.com'
#Commented
'''Commented
Commented
'''
```
##第二题：判断以下几个变量是否合法
```python
1a #error
$a #error
_b #correct 
a  #correct
```
##第三题：对于字符型，我是否可以全部转换为整型，请回答并给与原因
只含数字的可以，带其它字符的直接转换会报错。
##第四题：
`a='this is test. '`
第一小步，请去掉右边的空格，保存到变量b里面
第二小步，对b用空格进行切分，保存到c
第三小步，判断c是什么数据类型类型，并打印出c的个个值
第四小步，对a替换成'this is anying study.'
```python
#!/user/bin/env python
a = 'this is test. '
print a
b = a.strip()
print b
c = ' '.join(b)
print c
print type(c)
print c.split()
a = 'this is anything study.'
print a
```
```shell
#Result
this is test. 
this is test.
t h i s   i s   t e s t .
<type 'str'>
['t', 'h', 'i', 's', 'i', 's', 't', 'e', 's', 't', '.']
this is anything study.
```

##第五题，定义了一个变量名为 port 的列表，我想在里面依次添加22、80、23、8080、139、445、3389，然后进行正向（sort）排序，然后打印每个数值
```python
#!/user/bin/env python
port = []
print port
port.append(22)
print port
port.append(80)
print port
port.append(23)
print port
port.append(8080)
print port
port.append(139)
print port
port.append(445)
print port
port.append(3389)
print port
port.sort()
print port
```
```shell
#Result
[]
[22]
[22, 80]
[22, 80, 23]
[22, 80, 23, 8080]
[22, 80, 23, 8080, 139]
[22, 80, 23, 8080, 139, 445]
[22, 80, 23, 8080, 139, 445, 3389]
[22, 23, 80, 139, 445, 3389, 8080]
```
##第六题，写一个if语句，如果变量a小于5，则输出this is a fun，如果a小于10则输出this is a joke，如果a小于20则输出this is a test，如果都不成立，则输出this is last
```python
#!/user/bin/env python
a = input()
if a<5:
	print 'this is a fun'
elif a<10:
	print 'this is a joke'
elif a<20:
	print 'this is a test'
else:
	print 'this is last'
```
##第七题，python中，什么情况下为假。（不同数据类型下为假）
布尔型 false 就是假；
整形 浮点型 0 是假；
字符串、元组、列表等……**内容为空** 时表示假
```python
#!/user/bin/env python
a = 0
if a:
	print 'true!'
elif not a:
	print 'False!'

a = 1
if a:
	print 'true!'
elif not a:
	print 'False!'

a = []
if a:
	print 'true!'
elif not a:
	print 'False!'

a = [1]
if a:
	print 'true!'
elif not a:
	print 'False!'

a = False
if a:
	print 'true!'
elif not a:
	print 'False!'

a = 0.0
if a:
	print 'true!'
elif not a:
	print 'False!'

a = ''
if a:
	print 'true!'
elif not a:
	print 'False!'
```
```shell
#Result
False!
true!
False!
true!
False!
False!
False!
```
##第八题，元组和列表的有哪些共同点，那些不同点

元组：使用 () ，元组的值无法改变，无法创建单一元素的元组。
列表：使用 [] ，列表的值是可以改变的，可以创建单一元素列表。
  
  [1]: http://www.coffin5257.com