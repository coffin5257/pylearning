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