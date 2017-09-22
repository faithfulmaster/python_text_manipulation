
from sets import Set

# Receive a sentence as input separated by white spaces
print "Enter a sentence"
sentence = raw_input("> ")

# Split the sentences into words
words = sentence.split(' ')

# Sort and remove the duplicated words
newwords = sorted(set(words))

# Print it in the form of a sentence
newsentence = " ".join(newwords)
print newsentence
