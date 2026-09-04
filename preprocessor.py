import sys

inLink, outLink = sys.argv[1], sys.argv[2]
outputFile = open(outLink, 'w')
logFile = open('Code/log.log', 'w')

if inLink == "Code/-":
	outputFile.write("\\textcolor{red}{\\textit{TODO: This file is currently empty.}}")
	sys.exit(0)

try: inputFile = open(inLink, 'r')
except: outputFile.write("\\subsubsection{\\textcolor{red}{\\textbf{Error: File Not Found}}}")
TrustedOnly = (sys.argv[3] == "true")

outputFile.write("\\label{sec:" + inLink[5:].replace('/', '-').replace(' ', '_')[:-4] + "}" + '\n')

for line in inputFile.readlines():
	line = line.rstrip()
	if TrustedOnly:
		token, citation, depth, target = '', True, 0, 0
		res = ''
		for c in line:
			if c == '{' or c == '}' or c == ' ' or c == '\t': token = ''
			else: token += c
			if c == '{': depth += 1
			if c == '}': depth -= 1
			if citation: res += c
			if token == '\\citationneeded':
				citation, target = False, depth
				res = res[:-15]
			elif token == '\\todo':
				citation, target = False, depth
				res = res[:-5]
			elif not citation and depth == target: citation = True
			#print(res, c, token, citation, depth, target, file=logFile)
		line = res
	outputFile.write(line + '\n')