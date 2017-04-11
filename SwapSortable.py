def main():
	q = int(input().strip())
	for a0 in range(q):
		n = int(input().strip())
		a = list(map(int, input().strip().split(' ')))

		print("Yes" if swapSortable(a) else "No")

def swapSortable(array):
	justSwapped = False

	for i in range(1, len(array)):
		if array[i] <= array[i - 1]:
			if justSwapped:
				return False
			else:
				justSwapped = True
		else:
			justSwapped = False

	return True

if __name__ == "__main__":
	main()
