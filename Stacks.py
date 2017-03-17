# Prints the minimum cost for rearranging n items with an altitude and weight into k stacks.

def main():
	poles = []

	n, k = input().strip().split(' ')
	n, k = int(n), int(k)
	for i in range(n):
		xi, wi = input().strip().split(' ')
		poles.append(pole(int(xi), int(wi)))
	
	print(str(memoCost(poles, k)))

class pole:
	def __init__(self, altitude, weight):
		self.altitude = altitude
		self.weight = weight
	
	def move(self, other):	# Returns cost, resultant pole of moving this pole to another
		return (self.weight * (self.altitude - other.altitude)), pole(other.altitude, other.weight + self.weight)

def memoCost(poles, stacks):	
	table = [[-1] * stacks for i in range(len(poles))]

	def cost(poles, stacks):
		if len(poles) <= stacks:
			return 0	# Nothing to move
		elif stacks < 1:
			return float("inf")
		elif len(poles) == 2:	# Must move this pole
			return poles[-1].move(poles[-2])[0]	# Return cost only
		else:
			noMove = cost(poles[:-1], stacks - 1)

			p, s = len(poles) - 1, stacks - 1
			if table[p][s] < 0:
				moveCost, newPole = poles[-1].move(poles[-2])
				newPoles = poles[:-2]
				newPoles.append(newPole)

				move = moveCost + cost(newPoles, stacks)

				table[p][s] = move
			return min(noMove, table[p][s])
	
	return cost(poles, stacks)

if __name__ == "__main__":
	main()
