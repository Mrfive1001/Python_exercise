from sys import argv

script,filename = argv

print "We are going to erase %r."%filename
print "If you do not want that ,hit CTRL-C(^C)"
print "If you do want that, hit RETURN"
raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file.Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines"

line1 = raw_input("line1")
line2 = raw_input("line2")
line3 = raw_input("line3")

print "I am going to write these to the file."

target.write(line1+'\n')
target.write(line2+'\n')
target.write(line3+'\n')

print "And finally,we close it"
target.close()