# Demonstrates the bets to place and net result to expect at each level of a
# "best of 7" game series in order to end with a net result of either +$1000 or -$1000

def main():
	results = (
		(0, 0),	(1, 1),	(2, 2),	(3, 3),
		(1, 0),	(2, 0),	(3, 0),	(4, 0),
		(0, 1),	(0, 2),	(0, 3),	(0, 4),
		(1, 2),	(1, 3),	(1, 4),
		(2, 1),	(2, 3),	(2, 4),
		(3, 1),	(3, 2),	(3, 4),
		(4, 1), (4, 2),	(4, 3)
	)
	for result in results:
		wins = result[0]
		losses = result[1]

		print(
			("{0}\n"
			"Net: ${1:.2f}\n"
			"Bet: ${2:.2f}\n")
			.format(result, winnings(wins, losses), bets(wins, losses))
		)

def winnings(wins, losses):
	if wins >= 4:
		return 1000
	elif losses >= 4:
		return -1000
	else:
		return (winnings(wins + 1, losses) + winnings(wins, losses + 1)) / 2

def bets(wins, losses):
	if wins >= 4 or losses >= 4:
		return 0
	else:
		return (abs(winnings(wins + 1, losses) - winnings(wins, losses + 1))) / 2

if __name__ == "__main__":
	main()
