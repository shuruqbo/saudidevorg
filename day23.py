classroom1 = { "student1": "Mohammed", "student2": "Ali", "student3":" Salem" }
claasroom2 = { "studen1": "Areej", "student2": "Heba", "student3":" faten" }

print("list the students names")
print(classroom1.items(), claasroom2.items())
print("----------")

print('How many students in the first class?')
print(len(classroom1))
print("----------")

print("Asmaa wants to sign up for the seconed class!")
claasroom2["student4"] = "Asmaa" 
print(claasroom2.items())
print("----------")

print("is Mohammed a student in the seconed class?")
if "Mohammed" not in claasroom2:
	print("no, he is not")



