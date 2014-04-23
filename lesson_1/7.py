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