# Selects the time of 2 times which occurs first

def main():
	for i in range(int(input().strip())):
		t1, t2 = input().strip().split(' ')
		t1, t2 = [str(t1), str(t2)]
		print(timeCompare(t1, t2))

def timeCompare(t1, t2):
		if 'A' in t1 and 'A' in t2:
			if '12:' in t1 and not '12:' in t2:
				return "First"
			elif '12:' in t2 and not '12:' in t1:
				return "Second"
		elif 'P' in t1 and 'P' in t2:
			if '12:' in t1 and not '12:' in t2:
				return "First"
			elif '12:' in t2 and not '12:' in t1:
				return "Second"

		elif 'A' in t1 and 'P' in t2:
			return "First"
		elif 'A' in t2 and 'P' in t1:
			return "Second"

		for c1, c2 in zip(t1, t2):
			if c1.isdigit():
				c1, c2 = [int(c1), int(c2)]
				if c1 < c2:
					return "First"
				elif c2 < c1:
					return "Second"

if __name__ == "__main__":
	main()
