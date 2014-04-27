adict = {'a':54,'b':38,'c':79,'d':84}
for x in adict.keys():
	if adict[x] > 63:
		del adict[x]
print adict