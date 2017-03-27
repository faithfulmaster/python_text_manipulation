# Given input array of words
eng = ["whereas", "ok", "how", "elephant", "hello"]
print "Given array is ", eng

# Receive word input from user
print "Enter the word to be added at the last position"
word = raw_input("> ")

# Add new word to the end of existing array of words
neweng = " ".join(eng)
word = neweng + " " + word

word = word.split(' ')
print word
