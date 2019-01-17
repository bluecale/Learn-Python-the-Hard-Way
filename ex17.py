from sys import argv 
from os.path import isfile

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the outputfile exixt? %r" % isfile(to_file))
# create outfile if missing
if isfile(to_file) is False:
	of = open(to_file, "x")
	of.close()
	print("outfile %s created." % to_file)
	
print("Ready?. Hit RETURN to continue, CRTL-C to abort.")
input("? ")

out_file = open(to_file, "w")
out_file.write(indata)

print("Done!")

out_file.close()
in_file.close()


