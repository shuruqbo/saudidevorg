diction1 = { "name1" : "Ahmad", "name2" : "Asmaa", "name3": "Rose"}
print("dictionary keys and values")
print(diction1)
print("--------------")

#printing the value of a key
print("what is the value of the key name2")
x = diction1["name2"]
print(x)
print("what is the value of the key name3")
t = diction1.get("name3")
print(t)
print("--------------")


# changing the values of a key
diction1["name3"] = "Lily"
print(" peint the new dictionary")
print(diction1) 
print("--------------")

#looping through the dictionary
print(" keys:")
for s in diction1:
      print(s)
print("values")
for s2 in diction1:
      print(s2)
print("--------------")

# using item()  

print(" the dictionary Items")
print(diction1.items())          
