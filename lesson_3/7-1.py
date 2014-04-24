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