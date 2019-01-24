the_count = [1, 2, 3, 4, 5]
fruit = ["bananas", "pears", "oranges", "peaches"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for n in the_count:
	print("This is number %d" % n)
	
for f in fruit:
	print("Fruit of type %s" % f)
	
for c in change:
	print("I have %r" % c)
	
elements = []

for i in range(0, 6):
	print("Adding %d to list" % i)
	elements.append(i)
	
for e in elements:
	print("This is %d" % e)
