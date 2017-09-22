import csv
import re

# open usfm file for reading
f = open ('41MATULB.SFM','r')

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
addline = ""

d = f.readlines()
f.seek(0)
for line in d:
    if line == "\n":
        if addline:
            csvwriter.writerow([prev_book, prev_chapter, verse, addline])
            addline = ""
        continue
    elif line[0:3] == '\c ':
        if addline:
            csvwriter.writerow([prev_book, prev_chapter, verse, addline])
            addline = ""
        chapter = line[3]
        if chapter == prev_chapter:
            continue
        else:
            prev_chapter = chapter
    elif line[0:4] == '\id ':
        if addline:
            csvwriter.writerow([prev_book, prev_chapter, verse, addline])
            addline = ""
        book = line[4:]
        if book == prev_book:
            continue
        else:
            prev_book = book
    elif line[0:3] == '\\v ':
        if addline:
            csvwriter.writerow([prev_book, prev_chapter, verse, addline])
            addline = ""
        verse = line[3:5]
        addline = line[5:]
    elif line[0:4] == '\q2 ' or line[0:4] == '\q3 ':
        if line[4:] != " ":
            addline = addline[:-1] + line[4:]
    elif line[0:3] == '\q ' or line[0:3] == '\m ':
        if line[4:] != " ":
            addline = addline[:-1] + line[3:]
    prev_book = book
    prev_chapter = chapter


print "USFM to CSV conversion done!"

# close the usfm and csv file
f.close()
outfile.close()
