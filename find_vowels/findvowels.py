# To read the contents of the text file
filename = "sampletext.txt"
print "The file being read is: %r" % filename

txt = open(filename)
vowwords = []

print "\nThe contents of the file are:\n"
content = txt.read()
print content

# To find the vowels in the text and put them in a list
words = content.split(' ')

for i in words:
    if i[0] in 'aeiou':
        vowwords.append(i)

# To print the vowels
print vowwords
