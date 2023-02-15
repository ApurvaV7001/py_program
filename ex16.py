from sys import argv
script, filename=argv

print("we'r going to erase %r file"%filename)
print("If do yoy wan't that, hit CTRL-c(^)")
print("If you want that, hit RETURN")

input()("?")

print("Opening the file...")
target=open(filename,'w')

print("Truncating the file. 'GoodBye")
target.truncate()

print("Now i'm goning to ask you about three lines")
line1=input()("line1...")
line2=input()("line2...")
line3=input()("line3...")

print("I'm going to write these on file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And we closed it")
target.close()

