print "Enter a sentence"
sentence = raw_input("> ")

digits = 0
letters = 0

# To calculate number of letters and digits in a sentence
for i in sentence:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        letters += 1
    elif i.isdigit():
            digits += 1

print "The number of letters and digits in the given sentence are %d and %d respectively." % (letters, digits)
