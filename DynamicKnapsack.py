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
	table = [None * maxWeight]	# Init with infinity max value for each weight possibility
	weight = 0
	
	def solve(items):
		if len(items) <= 0:
			return 0
		
		newWeight = weight + items[0].weight
		if table[newWeight] is not None:
			next = items[0]
			remaining = items[1:]

			if newWeight > maxWeight:
				ta

	if next.weight <= maxWeight:
		return max(next.value + knapsack(remaining, maxWeight - next.weight), knapsack(remaining, maxWeight))
	else:
		return knapsack(remaining, maxWeight)

if __name__ == "__main__":
	main()
