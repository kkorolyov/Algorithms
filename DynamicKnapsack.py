# Displays the maximum value obtainable by taking items with a weight and value, constrained by a maximum weight.

def main():
	print("Max weight: ", end='')
	maxWeight = int(input())
	
	items = []

	print("Number of items: ", end='')
	for i in range(int(input())):
		print("VALUE WEIGHT: ", end='')
		value, weight = input().split(' ')
		value, weight = int(value), int(weight)
		items.append(item(value, weight))
	
	print(str(items))
	print(str(knapsack(items, maxWeight)))

class item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

	def __repr__(self):
		return "item({0}, {1})".format(self.value, self.weight)

def knapsack(items, maxWeight):
	results = {}
	
	def solve(items, weight):
		if len(items) <= 0 or weight > maxWeight:
			return 0
		
		if weight not in results:
			next = items[0]
			remaining = items[1:]

			results[weight] = max(solve(remaining, weight), next.value + knapsack(remaining, next.weight + weight))
		
		return results[weight]

	return solve(items, 0)

if __name__ == "__main__":
	main()
