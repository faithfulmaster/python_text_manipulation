# REceive user input on number of lines
print"How many lines do you want to enter?"
choice = int(input("> "))

lines =""

# Enter multiple lines
for i in xrange(choice):
    lines += raw_input() + "\n"

# Strip the extra new line and split the lines
lines = lines.strip()
lines = lines.split('\n')

# Capitalize each line
print "\nCapitalized lines are:"
for i in lines:
    print i.capitalize()
