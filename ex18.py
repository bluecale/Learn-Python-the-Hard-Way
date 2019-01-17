# this one is like your script with arguments
def print_any_number(*args):
	for x in range(len(args)):
		print("arg" + str(x + 1) + ": %r" % args[x])
	
# do this
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))
	
# this just takes one arguments
def print_one(arg1):
	print("arg1: %r" % arg1)
	
print_any_number("Yo", "Mo")
print_two_again("Yo", "Mo")
print_one("Yo") 