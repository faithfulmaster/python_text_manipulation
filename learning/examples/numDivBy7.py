# To print numbers between 900 and 2000 divible by 7, but not a multiple of 5
li = 900

print "Numbers between 900 and 2000 which are divisible by 7 but not a multiple of 5"
while li != 2000:
    if li % 7 == 0 and li % 5 != 0:
        print li,
    li += 1
