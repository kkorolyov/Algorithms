import sys, os.path, argparse, crypto

def shift(text, key):
	'''Encrypts text using shift substition
	
	text:	plaintext to encrypt
	key:	encryption key as a list of numbers

	return: encrypted string
	'''
	result = ""
	counter = 0

	for c in text:
		base = ord('A')	# Default to uppercase
		lBase = ord('a')
		end = ord('z')

		i = ord(c)	# ASCII value

		if base <= i <= end:	# Only shifts alphabetical characters
			if lBase <= i <= end:	# Lowercase
				base = lBase

			i = base + (i + key[counter % len(key)] - base) % 26	# Confine shift within 26 characters
			counter += 1

		result += chr(i)
	return result

def pad(text, key):
	'''Encrypts text using a one-time pad

	text:	plaintext to encrypt
	key:	encryption key as a list of numbers

	return:	encrypted string
	'''
	result = ""
	counter = 0

	for c in text:
		i = ord(c)	# ASCII value

		i = i ^ key[counter % len(key)]
		counter += 1

		result += chr(i)
	return result

def doubleTranspose(text, key):
	'''Encrypts text using double-transposition

	text: plaintext to encrypt
	key: encryption key as a list of numbers, where the first occurence of a number is in row permutations, 2nd in column permutations
	'''
	rows = []
	cols = []

	for n in key:
		if n in rows:
			cols.append(n)
		else:
			rows.append(n)

	result = ""
	matrix = []

	counter = 0
	for c in text:
		i = counter // len(cols)
		j = counter % len(cols)
		if j == 0:
			matrix.append([])
		matrix[i].append(c)
		counter += 1
	
	for i in range(min(rows), max(rows) + 1):
		for j in range(min(cols), max(cols) + 1):
			result += matrix[rows.index(i)][cols.index(j)]
	return result

def main():
	algorithms = {'SHIFT': crypto.shift,
								'PAD': crypto.pad,
								'DOUBLE_TRANSPOSE': crypto.doubleTranspose}

	def getParser():
		parser = argparse.ArgumentParser(description="Encrypts text using various encryption algorithms")
		parser.add_argument("text", help="text to encrypt")
		parser.add_argument("algorithm", type=str.upper, choices=algorithms.keys(), help="encryption algorithm to use")
		parser.add_argument("key", help="encryption key")
		parser.add_argument("-f", "--file", action="store_true", help="read text from a file specified by 'text'")
		parser.add_argument("-k", "--keyfile", action="store_true", help="read key from a file specified by 'key'")
		parser.add_argument("-o", "--output", help="output file")

		return parser

	# START
	parser = getParser()
	args = parser.parse_args()

	text = args.text
	if args.file:	# Read from file instead
		with open(text) as f:
			text = f.read()

	algorithm = args.algorithm
	key = None
	if args.keyfile:
		with open(args.key) as f:
			key = [int(n) for n in f.read().split(',')]	# Key may be arbitrary length
	else:
		key = [int(n) for n in args.key.split(',')]	# Key may be arbitrary length

	outFile = None
	if args.output:
		outFile = open(args.output, 'w')

	cipher = algorithms[algorithm](text, key)

	if outFile:
		outFile.write(cipher)
		outFile.close()
	print(cipher)

if __name__ == "__main__":
	main()
