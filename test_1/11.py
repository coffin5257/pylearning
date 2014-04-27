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