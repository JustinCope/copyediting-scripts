import re



def getResults(data, regex):
    exps = []
    for line in data:
        matches = regex.findall(line)
        for match in matches:
            exps.append(match)
    return exps

# exps.remove('$_$')

# define a frequency function here

def getFrequencies(exps):
    dict = {}
    for n in exps:
        if n not in dict.keys():
            dict[n] = 1
        else:
            dict[n] += 1
    return dict


# 	for each n in exps 
#      if n not key of dict
#         dict[n] = 1
#      else
#         dict[n] += 1


###########################################

sourceName = 'kamp-2016.v6.tex'

source = open(sourceName, 'r')

targetName = 'math.output.tex'


###########################################

searchA = re.compile(r'\$.+?\$')
searchB = re.compile(r'\\.+?_\\model')
searchC = re.compile(r'\$[^\$]+?_[^\$]+?\$')

search = searchA

###########################################


#output = sorted(list(set(getResults(source,search))))
output = sorted(getResults(source,search))
output2 = getFrequencies(output)

g = open(targetName, 'w')

g.write("\\documentclass[lucida]{sp} \n\n \\title{} \n \\author{\\spauthor{}} \n\n")

g.write("\\usepackage{drs} \n") 
g.write("\\usepackage{example} \n") 
g.write("\\usepackage{makecell} \n") 
g.write("\\usepackage{booktabs} \n") 
g.write("\\usepackage{moreenum} \n") 
g.write("\\usepackage{mathrsfs} \n \n") 

g.write("\\DeclareMathAlphabet{\\mathpzc}{OT1}{pzc}{m}{it} %\ Defines \mathpzc{} \n \n")

g.write("\\input{macros} \n")
g.write("\\input{drsrevised} \n\n")

g.write("\\begin{document} \n\n")

# for x in output:
# 	g.write(x)
# 	g.write("\n\n")

for w in sorted(output2, key=output2.get, reverse=True):
	g.write(w + "\hspace{\\fill}" + str(output2[w]) + "\n\n")

g.write("\\end{document}\n")

