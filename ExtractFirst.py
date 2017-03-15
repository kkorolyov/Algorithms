# Extracts the first occurrence of each distinct character in a string

def main():
	print("Input: ", end='')
	string = input()

	print("First distinct characters: {0}".format(extractFirsts(string)))

def extractFirsts(string):
	firsts = ""
	found = set()

	for c in string:
		if c not in found:
			found.add(c)
			firsts += c
	
	return firsts

if __name__ == '__main__':
	main()