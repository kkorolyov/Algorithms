# Displays all melodious (alternating consonants and vowels) words of length n

def main():
	print("Password length: ", end='')
	n = int(input().strip())

	words = melodious(n)

	for word in words:
		print(word)

def melodious(n):
	vowels = {'a', 'e', 'i', 'o', 'u'}
	consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}

	def makeWord(n, lastVowel):
		results = list(consonants if lastVowel else vowels)

		if n > 1:
			oldResults = results
			results = []
			for result in oldResults:
				for newResult in makeWord(n - 1, not lastVowel):
					results.append(result + newResult)

		return results

	return makeWord(n, True) + makeWord(n, False)

if __name__ == '__main__':
	main()
