# Given input array of words
eng = ["whereas", "ok", "how", "elephant", "hello"]
print "Given array is ", eng

elements = []

# insert and print words with length < 3 characters to a new list
for i in eng:
    if len(i) < 3:
        elements.append(i)

print "Words less than 3 characters in given array:"
print elements
