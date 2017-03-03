# Demonstrates the bets to place and net result to expect at each level of a
# "best of 7" game series in order to end with a net result of either +$1000 or -$1000

def main():
	games = 7
	expectedChange = 1000

	print("Total games [{0}]: ".format(games), end='')
	newGames = input()
	print("Expected change [${0:.2f}]: $".format(expectedChange), end='')
	newExpectedChange = input()

	if len(newGames) > 0:
		games = int(newGames)
	if len(newExpectedChange) > 0:
		expectedChange = float(newExpectedChange)

	calc = BetCalculator(games, expectedChange)

	print("{0} games, ${1:.2f} expected change".format(games, expectedChange), end='\n\n')
	
	print("Bets before")
	calc.print(calc.bets)
	print()
	print("Winnings after")
	calc.print(calc.winnings)

class BetCalculator:
	def __init__(self, games, expectedReturn):
		self.games = games
		self.bestOf = (games + 1) // 2
		self.expectedReturn = expectedReturn
	
	def winnings(self, wins, losses):
		if wins >= self.bestOf:
			return self.expectedReturn
		elif losses >= self.bestOf:
			return -self.expectedReturn
		else:
			return (self.winnings(wins + 1, losses) + self.winnings(wins, losses + 1)) / 2

	def bets(self, wins, losses):
		if wins >= self.bestOf or losses >= self.bestOf:
			return 0
		else:
			return (abs(self.winnings(wins + 1, losses) - self.winnings(wins, losses + 1))) / 2
		
	def print(self, fun):
		print("W\\L", end='')
		for i in range(self.bestOf + 1):
			print("\t{0}".format(i), end='')	# Losses columns
		print()

		for i in range(self.bestOf + 1):
			print("{0}".format(i), end='')	# Wins rows

			for j in range(self.bestOf + 1):
				print(
					"\t${0}".format(fun(i, j)) if (i + j <= self.games) else "\t",
					end=''
				)
			print()

if __name__ == "__main__":
	main()
