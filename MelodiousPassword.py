# Displays all melodious passwords of length n

def main():
	print("Password length: ", end='')
	n = int(input().strip())

	passwords = melodious(n)

	for password in passwords:
		print(password)

def melodious(n):
	vowels = {'a', 'e', 'i', 'o', 'u'}
	consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}

	def makePass(n, lastVowel):
		results = list(consonants if lastVowel else vowels)

		if n > 1:
			oldResults = results
			results = []
			for result in oldResults:
				for newResult in makePass(n - 1, not lastVowel):
					results.append(result + newResult)

		return results

	return makePass(n, True) + makePass(n, False)

if __name__ == '__main__':
	main()
