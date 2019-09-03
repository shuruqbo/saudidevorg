Firstlist = ["apples","oranges","bananas"]
print("1st list")
print(Firstlist)
#lenght
print(len(Firstlist))

#addtion

Firstlist.append("cherry")
print(Firstlist)

#copying the first list
Secondlist = Firstlist.copy()
Firstlist.insert(1,"grapes")
#copying the first list again
Thirdlist = list(Firstlist)
print(Firstlist)
Firstlist.remove("apples")
print(Firstlist)
Firstlist.pop(1)
print(Firstlist)
Firstlist.pop()
print(Firstlist)
Firstlist.clear()
print(Firstlist)
print("2nd list")
print(Secondlist)
print("3rd list")
print(Thirdlist)

# the use of (List method)
forthList = list(("burger", "chips", "cola"))
print("4th list")
print(forthList)