import csv
import re

fileread = open('1JN.csv')
reader = csv.reader(fileread, delimiter='\t')

wb = open('1JNoutput.usfm','w')
for row in reader:
    wb.write("\n\id " + row[0] + "\n\c " + row[1] + "\n\\v " + row[2] + " " +row[3])
wb.close()

prev_book = ""
prev_chapter = ""
chapter = ""
book = ""

f = open ('1JNoutput.usfm','r+')
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
            f.write(line)
    elif line[0:4] == '\id ':
        book = line[4]
        if book == prev_book:
            continue
        else:
            f.write(line)
    else:
        f.write(line)
    prev_book = book
    prev_chapter = chapter

f.truncate()
f.close()
fileread.close()
print "Conversion from csv to usfm done !"
