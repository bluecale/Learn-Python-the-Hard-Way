from sys import argv 
from os.path import isfile

script, from_file, to_file = argv

open(to_file, "w").write(open(from_file, "r").read())