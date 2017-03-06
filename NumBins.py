# Calculates the number of binary strings of length N without consecutive 1's

def main():
	print("Length: ", end='')
	n = int(input())

	print(numBins(n))
	print(numBinsIter(n))

def numBins(n):
	if n < 1:
		return 1
	elif n == 1:
		return 2
	else:
		return numBins(n - 1) + numBins(n - 2)
def numBinsIter(n):
	results = [1, 2]

	for i in range(2, n + 1):
		results[i % 2] = results[0] + results[1]

	return results[n % 2]

if __name__ == '__main__':
	main()
