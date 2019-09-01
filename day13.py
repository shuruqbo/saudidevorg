floatNumbers = [1.5, 2.3, 5.7, 9.8]
print("original list:")
print(floatNumbers)
print("print seconed Item")
print(floatNumbers[1])

print("loop through the items")

for x in floatNumbers:
       print(x)

print("change third item")
floatNumbers[2] = "SDO"
print(floatNumbers)

print("delete the forth item")
del floatNumbers[3]
print(floatNumbers)
