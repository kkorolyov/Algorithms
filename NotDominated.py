# Calculates the number of 2D points in set that are not "dominated" in x and y values by another points

def main():
	points = [
		(1, 1),
		(0, 0),
		(13, 45),
		(2, 3),
		(14, 2)
	]
	num = str(notDominated(points))
	print(num)

def notDominated(points):
	points = sorted(points, key=pointsX)
	last = len(points) - 1
	
	maxY = points[last][1]
	num = 1
	for i in range(last - 1, 0, -1):
		if points[i][1] >= maxY:
			num += 1
			maxY = points[i][1]
	return num
def pointsX(point):
	return point[0]

if __name__ == '__main__':
	main()
