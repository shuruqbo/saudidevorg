#original set
print("part1")
set1 = {1,3,5,7,8}
print(set1)
print("---------")
#adding items
set1.update((4,8,12))
print("set after addint new items")
print(set1)
print("---------")
#deleting an item
set1.remove(8)
print(set1)
print("---------")
set1.clear()
print(set1)
print("-----------------------------------")
print("part2")
dictionary1 = {"name":"pigeon", "type": "bird", "skin cover":"feather"}
print(dictionary1)
print("the value of the key 'type'")
x = dictionary1.get("type")
print(x)
print("---------")
print("changing the value of 'skin cover'")
dictionary1["skin cover"] = "hair"
print(dictionary1)