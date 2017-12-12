try:
	a = 20/0
	raise NameError("Can not devide by 0")
except NameError as e:
	print "Can not devide by 0"
	print e
