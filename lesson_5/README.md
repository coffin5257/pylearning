**1、python 函数中的形参和实参的区别是什么？**

形参就是函数的位置参数，表示函数的数据入口，只在函数内部发挥作用。
实参是实际的参数，在调用函数时，实参的值会传给形参。

**2、python函数是否可以设置形参的默认值？如果不可以，为什么？如果可以，如何设置？**

可以的。
def fun_name(参数名=默认值)

**3、定义一个函数，该函数接收两个整型参数，并输出较大的那个值。**
```python
#!/usr/bin/env python
def com(a,b):
	if a > b:
		print a
	else:
		print b
x,y = raw_input().split()
com(x, y)
```