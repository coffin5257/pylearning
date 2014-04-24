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