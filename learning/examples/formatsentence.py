# To put question mark after the interrogative words
# and full stops otherwise in a given sentence

inter = {'what', 'when', 'where', 'whom', 'who', 'why', 'how'}
print "Enter a sentence: "
line = raw_input("> ")
words = line.split(' ')
newwords = []

# Checking for interrogative words
for j in words:
    if j in inter:
        j = j + "?"
        newwords += j,
    else:
        j = j + "."
        newwords+= j,

newline = " ".join(newwords)
print newline
