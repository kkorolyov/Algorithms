import codecs, crypto, itertools

def buildTransposeKeys():
	transposeKeys = []

	transposeRows = list(itertools.permutations([1, 2, 3, 4]))	# Assume 8-letter word either in 4x2 or 2x4
	transposeCols = list(itertools.permutations([1, 2]))
	for row in transposeRows:
		for col in transposeCols:
			transposeKeys.append(row + col)	# 4x2 matrix
			transposeKeys.append(col + row)	# 2x4 matrix

	return transposeKeys

def buildDictionary():
	words = []

	with codecs.open('words', 'r', 'utf-8') as f:
		for word in f:
			trimmed = word.rstrip('\n')
			if (len(trimmed) == 8):	# Only need 8-letter words
				words.append(trimmed)
	
	return words

dictionary = buildDictionary()
cipher = 'LWHFQHDS'	# Lazy input method
shiftKeys = list(range(26))	# 0-25 for substitution keys
transposeKeys = buildTransposeKeys()

for shiftKey in shiftKeys:
	shiftedCipher = crypto.shift(cipher, [shiftKey])

	for transposeKey in transposeKeys:
		result = crypto.doubleTranspose(shiftedCipher, transposeKey).lower()	# Dictionary words lowercase
		if result in dictionary:
			print(result.upper(), "ShiftKey=" + str(shiftKey), "TransposeKey=" + str(transposeKey))


