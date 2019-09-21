# fibonacci sequence of numbers 
# refrence: https://www.tutorialgateway.org/python-fibonacci-series-program/ 
userInput = int(input("Enter a number: "))

value1 = 0
value2 = 1

for x in range(0, userInput):
	if (x <= 1):
		theNumber = x
	else:
		theNumber = value1 + value2
		value1 = value2
		value2 = theNumber

	print(theNumber)	