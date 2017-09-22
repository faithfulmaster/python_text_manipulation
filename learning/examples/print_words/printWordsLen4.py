prompt = '> '

# receive string input fromu user
print "Enter a string:"
sentence = raw_input(prompt)

# split the string into words
word = sentence.split(' ')
elements = []

# append and print words with length < 4 characters to a new list
for i in word:
    if len(i) < 4:
        elements.append(i)

print elements
