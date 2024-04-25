import random
import string
import re
import sys

#> python3 PS1obfuscate.py myfile.ps1 [-E] [-C] [-F] [-V] [-S]

if len(sys.argv) <= 1 :
	print("[!] Please provide a file.")
	print("[EXAMPLE] > python3 PS1obfuscate.py myfile.ps1 [-E] [-C] [-F] [-V] [-S]")
	print("-E 	Remove empty lines")
	print("-C 	Remove comments 	(remove comments starting with # and blocs such as <# ... #>)")
	print("-F 	Rename functions 	(rename functions with random strings)")
	print("-V 	Rename variables 	(rename variables with random strings)")
	print("-S 	Split strings 		('MyVariable' --> 'My'+'Va'+'ri'+'ab'+'le')")
	print("(applies all if no option specified)")
	print("-h 	Show options")
	sys.exit()

if '-h' in sys.argv :
	print("[EXAMPLE] > python3 PS1obfuscate.py myfile.ps1 [-E] [-C] [-F] [-V] [-S]")
	print("-E 	Remove empty lines")
	print("-C 	Remove comments 	(remove comments starting with # and blocs such as <# ... #>)")
	print("-F 	Rename functions 	(rename functions with random strings)")
	print("-V 	Rename variables 	(rename variables with random strings)")
	print("-S 	Split strings 		('MyVariable' --> 'My'+'Va'+'ri'+'ab'+'le')")
	print("(applies all if no option specified)")
	print("-h 	Show options")
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
		
	if '-E' in sys.argv or default :
		script = removeEmptyLines(script)

	if '-S' in sys.argv or default :
		script = splitStrings(script)

	outputfilename = file.split('.')[0] + '-OBFUSCATED.ps1'

	with open(outputfilename, "w") as outputfile:
		outputfile.write(script)
		print("[+] File written to " + outputfilename)

#Returns a string with all the strings splitted
def splitStrings(content):
	print("[+] Splitting strings")
	list_strings = getStrings(content)
	for string in list_strings[0]:
		content = content.replace('"' + string + '"',splitSingleString(string,'double'))
	for string in list_strings[1]:
		content = content.replace("'" + string + "'",splitSingleString(string,'simple'))
	return content

#Returns a splitted representation of a string
#Ex1: 'hello' --> 'h'+'e'+'l'+'l'+'o'
#Ex2: "there" --> "t"+"h"+"e"+"r"+"e"
def splitSingleString(string, quoted):
	if string == "":
		return ""
	else:
		splitter = 2 #Make groupes of 2 chars
		if quoted == 'simple':
			groupes = [string[i:i+splitter] for i in range(0, len(string), splitter)]
			result = "+".join("'" + groupe + "'" for groupe in groupes)
			
		elif quoted == 'double':
			groupes = [string[i:i+splitter] for i in range(0, len(string), splitter)]
			result = "+".join("'" + groupe + "'" for groupe in groupes)
	return result

#Returns a list of all strings
def getStrings(string):
	pattern = re.compile(r'=\s*\"(.*)\"')
	list_strings_double_quote = pattern.findall(string)
	result1 = list(set(list_strings_double_quote)) #remove duplicas

	pattern2 = re.compile(r"=\s*\'(.*)\'")
	list_strings_simple_quote = pattern2.findall(string)
	result2 = list(set(list_strings_simple_quote)) #remove duplicas

	return result1,result2

#Returns a string with empty lines removed
def removeEmptyLines(content):
	print("[+] Removing empty lines")
	result = ""
	for line in content.splitlines():
		if not line == "" and not line.replace(" ","") == "" and not line == None:
			result = result + "\n" + line
	return result

#Returns a string with modified functions
def renameFunctions(string):
	print("[+] Renaming functions")
	functions = getFunctions(string)
	for function in functions :
		string = string.replace(function,getRandomString(12))
	return string

#Returns a list of all script functions names
def getFunctions(string):
	pattern = re.compile(r'[Ff]unction\s+(?:\w*:)*([a-zA-Z_]\w*-*_*\w*)\s*(?:\(.*\))*\s*{')
	list_functions = pattern.findall(string)
	result = list(set(list_functions)) #remove duplicas
	return result

#Returns a string with modified variables
def renameVariables(string):
	print("[+] Renaming variables")
	string = lowerVariables(string)
	variables = getVariables(string)
	for variable in variables :
		randomstring = getRandomString(10)
		string = string.replace('$' + variable,'$' + randomstring)
	return string

#Returns a string with all variables lowered
def lowerVariables(string):
	list__all_variables = re.findall(r'\$(\w+)\s*', string)
	result = []
	for element in list__all_variables:
		if element not in result:
			result.append(element)
	result.sort(key=len, reverse=True)
	for element in result:
		string = string.replace('$' + element, '$' + element.lower())
	return string

#Returns a list of all script variables that are not functions parameters
def getVariables(string):
	list_variables = re.findall(r'\$(\w+)\s*=', string)
	result = list(set(list_variables)) #remove duplicas
	result.sort(key=len, reverse=True) #sorted by len to prevent erasing other variables with the same name
	return result

#Returns a string without the new-line comments
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
