import re
x = " please, I want {} sandwitches and {} donoutes "

print("example 1: ")
print(x.format(5,7).replace("I","we").replace("a","A"))
# another way to do the capital A replacment 
change_to_upper = 'a'
input = re.sub(change_to_upper, change_to_upper.upper(), x.format(5,7).replace("I","we"))
print("example 2:")
print(input)

