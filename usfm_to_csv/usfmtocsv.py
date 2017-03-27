import csv
import re

# open usfm file for reading
f = open ('1JNInput.usfm','r')

# open csv file for writing
outfile = open('1JNOutput.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(outfile, delimiter ='\t')

# Writing to csv file
prev_book = ""
prev_chapter = ""
chapter = ""
book = ""
verse = ""

d = f.readlines()
f.seek(0)
for line in d:
    if line == "\n":
        continue
    elif line[0:3] == '\c ':
        chapter = line[3]
        if chapter == prev_chapter:
            continue
        else:
            prev_chapter = chapter
    elif line[0:4] == '\id ':
        book = line[4:]
        if book == prev_book:
            continue
        else:
            prev_book = book
    elif line[0:3] == '\\v ':
        verse = line[3:5]
        csvwriter.writerow([prev_book, prev_chapter, verse, line[5:]])

    prev_book = book
    prev_chapter = chapter


print "USFM to CSV conversion done!"

# close the usfm and csv file
f.close()
outfile.close()
