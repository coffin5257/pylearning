**第一题：**
1 添加字符串'jay'到集合a里。
2 集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集。
```pyhthon
a.add('jay')
a|b
(a^b)|(a&b)
```

**第二题：**
已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：
1 添加字符串对象'abc'到集合setinfo
2 删除集合setinfo里面的成员m
3 求2个集合的交集和并集
```python
setinfo.add('abc')
setinfo.remove('m')
setinfo&finfo
setinfo|finfo
```

**第三题：**
已知列表a=[1,14,6,8,9,18]和b=[14,9,16,15,13,3],我们测试对应的键相加，比如a的0键a[0]+b[0]，a[1]+b[1]。打印出数据，输出的数据不能重复
```python
a = [1,14,6,8,9,18]
b = [14,9,16,15,13,3]
c = []
for x in range(len(a)):
	c.append(a[x]+b[x])
print c
```
