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