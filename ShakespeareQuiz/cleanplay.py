
import sys 
from cleanheader import *

in_file = sys.argv[1]

fin = open(in_file, 'r')
fout = open("clean.txt", 'w')

header_fout = open("noHeader.txt", 'w')
cleanHeader(fin, header_fout)

header_fout = open("noHeader.txt", 'r')


def cleanPlay(header_fout, fout):
	#gets the name of the play#
	fin = header_fout
	firstLine = fin.readline()
	
	a = 'of'
	b = 'by'
	
	name = firstLine.split(a)[-1].split(b)[0]
	fout.write(str(name+'\n'))

	lines = fin.readlines()

	#footer
	lines = lines[:-3]
	for ch in lines:
		if ch == '\n':
			pass
		else:
			fout.write(ch)

	#cleaning up a little more
	for line in lines:
		#songs
		if line[0] == ' ' and line == line.upper():
			pass
		#directions
		elif line[0] == '[' or line[-1] == ']':
			pass
		#blanks
		elif line[0] == '\n':
			pass

		else:
			fout.write(line)

	fin.close()
	fout.close()

cleanPlay(header_fout, fout)

