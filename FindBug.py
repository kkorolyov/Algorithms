# Prints the coordinate of the first bug "X" in an array of strings

def main():
	n = int(input().strip())
	grid = []
	for i in range(n):
		grid.append(str(input().strip()))
	
	print(",".join(map(str, findBug(grid))))

def findBug(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (grid[i][j] == 'X'):
				return (i, j)

if __name__ == "__main__":
	main()
