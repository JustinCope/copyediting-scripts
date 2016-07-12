import re
import sys

def getResults(data, regex):
    exps = []
    for line in data:
        matches = regex.findall(line)
        for match in matches:
            exps.append(match)
    return exps

def getFrequencies(exps):
    dict = {}
    for n in exps:
        if n not in dict.keys():
            dict[n] = 1
        else:
            dict[n] += 1
    return dict

###########################################

source = sys.argv[1] # LaTeX file to search
target = sys.argv[2] # Name for the output file

# Check for custom regex from terminal input, otherwise default to math delimiter search
if len(sys.argv) == 4:
	regex = sys.argv[3]
else:
	regex = '\$.+?\$'

regexComplete = r'{0}'.format(regex)

search = re.compile(regexComplete)
	
source = open(source, 'r')

output = getFrequencies(getResults(source,search))

g = open(target, 'w')

g.write("\\documentclass{article} \n \\input{frontmatter} \n \\begin{document} \n\n")

for w in sorted(output, key=output.get, reverse=True):
	g.write(w + "\hspace{\\fill}" + str(output[w]) + "\n\n")

g.write("\\end{document}\n")

