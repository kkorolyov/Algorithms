def main():
	word = input().strip()

	print("Yes" if valid(word) else "No")

def valid(word):
	word = word.upper()
	vowels = {"A", "E", "I", "O", "U", "Y"}

	for i in range(1, len(word)):
		if (word[i] == word[i - 1]) or (word[i] in vowels and word[i - 1] in vowels):
			return False

	return True

if __name__ == "__main__":
	main()
