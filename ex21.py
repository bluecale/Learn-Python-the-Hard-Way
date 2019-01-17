def add(a, b):
	print("Adding %d and %d" % (a, b))
	return a + b

def subtract(a, b):
	print("Subrtacting %d form %d" % (a, b))
	return b - a
	
def multiply(a, b):
	print("Multiplying %d by %d" % (a, b))
	return a*b
	
def divide(a, b):
	print("Dividing %d by %d" % (a, b))
	return a/b
	
print("Lets do some maths with functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight:%d, IQ: %d" % (age, height, weight, iq))