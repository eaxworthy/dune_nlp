'''
Reads pdfs and returns a text file. Will not work for all pdfs.
Call via: python read_pdfs.py <input file in data folder> <output file>
'''
import PyPDF2 as pf
import sys
import re

#check for file names
if len(sys.argv) != 3:
    print('Incorrect script call.')
    exit()

#read in pdf
in_file = sys.argv[1]
reader = pf.PdfFileReader('./data/' + in_file)

#get number of pages
page_count = reader.numPages
print(page_count)
#set output name
out_file = sys.argv[2]
output_file = out_file

with open(output_file, 'w') as output:
    for i in range(page_count):
        page = reader.getPage(i)

        #pdf specific cleaning. change according to needs
        #page = re.sub(" +", " ", page.extractText())
        #page = re.sub("\. \. \.", "...", page)
        #page = re.sub("\n", "", page)

        output.write(page.extractText())
