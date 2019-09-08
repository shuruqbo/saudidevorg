Set1 = {1,2,3,3,"cat", "mouse", 'cat'}

print(Set1)
print(" is 1 in the set?")
print(1 in Set1)
print("--------")
# adding one item

Set1.add("dog")
print(Set1)
print("--------")
# adding many items
Set1.update([4,8,6])
print(Set1)