# Take htwo digits as inputs
print "Enter any two digits"
row = int(raw_input("> "))
col = int(raw_input("> "))

elements = []

print "\nThe %d X %d 2-D array generated is:" % (row, col)

# To generate a 2-D array of size (row X col)
for i in range(row):
    for j in range(col):
        elements.append(j*i)
    print elements,
    elements = []
    print ""
