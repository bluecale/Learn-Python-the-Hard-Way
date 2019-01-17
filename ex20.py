from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())
	
def rewind(f):
	f.seek(0)
	
def print_a_line(f, line_number):
	print(line_number, f.readline())
	
current_file = open(input_file)

print("All file:")
print_all(current_file)

print("Rewind")
rewind(current_file)

print("Let's print three lines\n")

current_line = 0
for x in range(3):
	current_line += 1
	print_a_line(current_file, current_line)
	
	
	
	
