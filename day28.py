# a code for a shoping list
itemsset = []
items = input("enter item, or enter done ")
while  items != "done":
    itemsset.append(items)
    items = input("next item, or enter done ")
if items == "done":
	numberofitems = len(itemsset) 
	print("------------------------------")
	print(" ")
	print("you have ", numberofitems," items, here is your list")
	print(itemsset)
