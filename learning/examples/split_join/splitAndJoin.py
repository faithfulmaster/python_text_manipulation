# Receive string input fromu user
print "Enter a string:"
sentence = raw_input("> ")

# Split the string into words
word = sentence.split(',')

# Sort the words and join in it into a comma separated sentence
word.sort()
elements = ','.join(word)

print "\nOutput string is:"
print elements
