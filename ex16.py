from sys import argv 

script, filename = argv 

print("We are going to erase %r." % filename)
print("If you don't want that, hit CRTL-C (^C).")
print("If ok, hit Return.")

input("? ")

print("Opening the file...")
target = open(filename, "w")

print("truncating...Bye!")
target.truncate()

print("Now i am going to ask you three lines:")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Rewriting file...")

target.write(line1 + "\n" + line2 + "\n" +line3)

print("Now we close.")

if target.close():
	print("done")