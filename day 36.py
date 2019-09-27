def thisFunc(n):
	return lambda a : a * n

mydoubler = (thisFunc(2))
print(mydoubler(11))


