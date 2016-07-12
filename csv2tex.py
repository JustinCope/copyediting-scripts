import csv
import sys

name = sys.argv[1]

file = open(name,'r')
reader = csv.reader(file)

table = []
for n in reader:
     table.append(n)

# Get the table's dimensions
colNum = len(table[0])
rowNum = len(table)

# Create the string that will specify the number of columns in the LaTeX source
colSpec = "l" * colNum
colSpecBrak = "{" + colSpec +"}"

output = open(name+'.tex', 'w')

print>>output, "\\begin{tabular}" + colSpecBrak

for n in table:
	for x in n[:-1]:
		print>>output, x + " & "
	
	print>>output, n[-1] + " \\\\"

print>>output, "\\end{tabular}"
	
