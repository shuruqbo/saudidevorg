#function 1
def thisFunction(fruits):
    for x in fruits:
	    print(x)
f = [ "banana", "ornges", " apples"]
thisFunction(f)
print("-----")

# function 2
def thisFunction2(x):
	return x * 3
print(thisFunction2(2))	
print("-----")

# function 3
def thisFunction3(*kids):
    print(kids)
thisFunction3("sara", "mohammed ", "ahmad")
print("-----")

# function 4
def thisRecursion(rec):
	if(rec > 0):
		results = rec + thisRecursion(rec-1)
		print(results)
	else:
		results = 0
	return results
print("recursion example:")
thisRecursion(8)	
