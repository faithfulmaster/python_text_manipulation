# Given input array of words
eng = ["test", "ok", "how", "why", "hello"]
print "Given array is ", eng

# Receive word input from user
print "Enter the word to be added at the first position"
word = raw_input("> ")

# Add new word to the start of existing array of words
neweng = " ".join(eng)
word = word + " " + neweng

word = word.split(' ')

# Print the new array of words
print word
