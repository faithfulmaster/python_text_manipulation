from bs4 import BeautifulSoup
import re
import csv

soup = BeautifulSoup(open("1.htm"), "lxml")

outfile = open('output.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(outfile, delimiter ='\t')
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""

table = soup.find_all("table", attrs={"class":"tablefloatheb"})
print "Parsing HTML file"

# The first tr contains the field names.
for t in table:
    for row in t.find_all("tr"):
        for item in row.find_all('span', class_= 'eng'):
            a = item.get_text().encode('utf-8')
        for item in row.find_all('span', class_= 'refheb'):
            b = item.get_text().encode('utf-8')
        for item in row.find_all('span', class_= 'strongsnt'):
            c = item.get_text().encode('utf-8')
        for item in row.find_all('span', class_= 'hebrew'):
            d = item.get_text().encode('utf-8')
        for item in row.find_all('span', class_= 'translit'):
            e = item.get_text().encode('utf-8')
        for item in row.find_all('span', class_= 'strongs'):
            f = item.get_text().encode('utf-8')
        csvwriter.writerow([a, b, c, d, e, f])

outfile.close()
