第三课作业：
================
#My Blog: [灵柩里的人][1]

 [1]: http:www.coffin5257.com


 **1、用两种方式创建一个键为 name age height 的字典**
 ```python
 info = dict(name=None,age=None,height=None)
 info = {'name':None,'age':None,'height':None}
 ```

 **2、纠错**
```python
 b=（'A':1,'B':2） #()改为{}
 a=｛'A'=>1,'B'=>2｝ # => 改为 :
 a={1,'B':2} # 1 缺少一个键值
 a={'A','B'} # 键A B 需要有初始值
 a={'A':1,'B':2}
 printa[1] #按键值来索引 应该是print a['A']
```
**3、给一个元组:** `a = ('name','age','height')`
```python
bdict = {}.fromkeys(a)
```

 **4、创建两个字典，合并两个字典**
```python
adict = dict(name='coffin',age=99)
bdict = dict(sex='male',int='hack')
cdict = dict(adict.items() + bdict.items())
```
**5、已知字典：** `ainfo = {'ab':'liming','ac':20}`
(1)使用2个方法，输出：`ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}`
```python
方法一：
ainfo['sex'] = 'man'
ainfo['age'] = 20
print ainfo

方法二：
binfo = {'sex':'man','age':20}
print dict.update(ainfo)
```python
(2)输出结果：['ab','ac']
ainfo.keys()
(3)输出结果：['liming',20]
ainfo.values()
(4)通过2个方法返回键名ab对应的值
```python
ainfo['ab']
ainfo.pop('ab')
```
(5)通过2个方法删除键名ac对应的值
```python
ainfo.pop('ac')
del ainfo['ac']
```




#3天内的集训题

**1、列表**
`a = [11,22,24,29,30,32]`
1 把28插入到列表的末端
`a.append(28)`
2 在元素29后面插入元素57
`a.insert(4,57)`
3 把元素11修改成6
`a[0]=6`
4 删除元素32
`a.remove(32)`
5 对列表从小到大排序
`a.sort()`

**2、列表**
`b = [1,2,3,4,5]`
1 用2种方法输出下面的结果：`[1,2,3,4,5,6,7,8]`
方法一：
```python
b.append(6)
b.append(7)
b.append(8)
print b
```
方法二：
```python
t = [6,7,8]
print b+t
```
2 用列表的2种方法返回结果：`[5,4]`
```python
方法一：
b[:-3:-1]
方法二：
b.reverse()
b[:2]
```
3 判断2是否在列表里
```python
2 in b
#True
```
**习题3：**`b = [23,45,22,44,25,66,78]`
**用列表解析完成下面习题：**
1 生成所有奇数组成的列表
```python
#!/usr/bin/env python
b = [23,45,22,44,25,66,78]
a = []
for x in b:
	if x%2 == 1:
		a.append(x)
print a
```
2 输出结果:`['the content 23','the content 45']`
```python
print ['the content %s'% x for x in b[:2]]
```
3 输出结果: [25, 47, 24, 46, 27, 68, 80]
```python
for x in range(len(b)):
	b[x]+=2
print b
```
**习题4：用range方法和列表推导的方法生成列表：**``[11,22,33]``
```python
#!/usr/bin/env python
a = []
for x in range(11,34):
	if x%11==0:
		a.append(x)
print a
```

**习题5：已知元组:** `a = (1,4,5,6,7)`
1 判断元素4是否在元组里
``4 in a``
2 把元素5修改成8
```python
#!/usr/bin/env python
a = (1,4,5,6,7)
a = a[0],a[1],8,a[-2],a[-1]
```
**习题6：已知集合:** `setinfo = set('acbdfem')`
**和集合**`finfo = set('sabcdef')`
**完成下面操作：**
1 添加字符串对象'abc'到集合setinfo
```python
setinfo.add('abc')
```
2 删除集合setinfo里面的成员m
```python
setinfo.remove('m')
```
3 求2个集合的交集和并集
```python
setinfo & finfo
setinfo | finfo
```
**习题7：用字典的方式完成下面一个小型的学生管理系统。**
1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
比如定义2个同学：

姓名：李明，年龄25，考试分数：语文80，数学75，英语85

姓名：张强，年龄23，考试分数：语文75，数学82，英语78

2 给学生添加一门python课程成绩，李明60分，张强：80分

3 把张强的数学成绩由82分改成89分

4 删除李明的年龄数据

5 对张强同学的课程分数按照从低到高排序输出。

6 外部删除学生所在的城市属性，不存在返回字符串 beijing
```python
#!/usr/bin/env python
#encoding:utf-8
liming = {'name':'李明','age':25,'city':'beijing','chinese':80,'math':75,'english':85}
zhangqiang = {'name':'张强','age':23,'city':'beijing','chinese':75,'math':82,'english':78}
print liming
print zhangqiang

liming['python'] = 60
zhangqiang['python'] = 80
print liming
print zhangqiang

zhangqiang['math'] = 89
print liming
print zhangqiang

del liming['age']
print liming
print zhangqiang

tmp = [zhangqiang['chinese'],zhangqiang['math'],zhangqiang['english'],zhangqiang['python']]
tmp.sort()
print tmp

del liming['city']
del zhangqiang['city']
```