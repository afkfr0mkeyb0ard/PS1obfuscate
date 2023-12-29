import random
import string
import re
import sys

#> python3 PS1obfuscate.py myfile.ps1 [-C] [-F] [-V]

if len(sys.argv) <= 1 :
    print("[!] Please provide a file.")
    print("[EXAMPLE] > python3 PS1obfuscate.py myfile.ps1 [-C] [-F] [-V]")
    print("-C 	Remove comments")
    print("-F 	Rename functions")
    print("-V 	Rename variables")
    print("(applies all if no option specified)")
    print("-h 	Show options")
    sys.exit()

if '-h' in sys.argv :
	print("[EXAMPLE] > python3 PS1obfuscate.py myfile.ps1 [-C] [-F] [-V]")
	print("-C 	Remove comments")
	print("-F 	Rename functions")
	print("-V 	Rename variables")
	print("(applies all if no option specified)")
	sys.exit()

file = sys.argv[1]

default = len(sys.argv) == 2

def main():
	script = getFileContent(file)
	print("[+] Working with file " + file)

	if '-C' in sys.argv or default :
		script = removeComments(script)

	if '-F' in sys.argv or default :
		script = renameFunctions(script)
	
	if '-V' in sys.argv or default :
		script = renameVariables(script)
	
	outputfilename = file + '_OBF'
	with open(outputfilename, "w") as outputfile:
		outputfile.write(script)
		print("[+] File written to " + outputfilename)
	
#Returns a string with modified functions
def renameFunctions(string):
	print("[+] Renaming functions")
	functions = getFunctions(string)
	for function in functions :
		string = string.replace(function,getRandomString(12))
	return string

#Returns a list of all script functions names
def getFunctions(string):
    pattern = re.compile(r'\b[Ff]unction\s+([a-zA-Z_]\w*-*\w*)\s*{')
    list_functions = pattern.findall(string)
    result = list(set(list_functions)) #remove duplicas
    return result

#Returns a string with modified variables
def renameVariables(string):
	print("[+] Renaming variables")
	variables = getVariables(string)
	for variable in variables :
		string = string.replace(variable,'$' + getRandomString(10))
	return string

#Returns a list of all script variables
def getVariables(string):
    list_variables = re.findall(r'\$[a-zA-Z0-9_]+', string)
    result = list(set(list_variables)) #remove duplicas
    return result

#Returns a string without the script PS comments
def removeComments(string):
	print("[+] Removing comments")
	result = re.sub(r'<#.*?#>', '', string, flags=re.DOTALL)
	result = re.sub(r'^\s*#.*$', '', result, flags=re.MULTILINE)
	return result

#Returns the content of a file
def getFileContent(path):
	file = open(path,'r')
	content = file.read()
	return content

#Returns a list of all the lines of a file
def getFileLines(path):
	with open(path) as file:
	    lines = [line.rstrip() for line in file]
	return lines

#Returns a random strings containing lowercases and uppercases
def getRandomString(length):
	result = ''.join(random.choice(string.ascii_letters) for i in range(length))
	return result

if __name__ == '__main__':
	main()
