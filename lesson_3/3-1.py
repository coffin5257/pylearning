#!/usr/bin/env python
b = [23,45,22,44,25,66,78]
a = []
for x in b:
	if x%2 == 1:
		a.append(x)
print a

print ['the content %s'% x for x in b[:2]]

for x in range(len(b)):
	b[x]+=2
print b