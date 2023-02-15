from sys import argv
from os.path import exists

script, from_file, to_file= argv

print("copying from %s to %s"%(from_file, to_file))

in_file=open(from_file)
indata-in_file.read

print("Input file is %d bytes long"%len(indata))

print("Does the output file exist? %r"%exists(to_file))
print("ready to hit RETURN to continue CTRL-C abort")
input()
out_file=open(to_file,'w')
out_file.write(indata)

print("Alright Alldone")
out_file.close()
in_file.close()