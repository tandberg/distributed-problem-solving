def maxEdges(nodelist):
	maximum = 0
	for node in nodelist:
		maximum = max(maximum, len(node.edges))

	return maximum

# def changecolors(leaders, nonleaders):
# 	for key in leaders:
# 		leaders[key].setColor('red')

# 	for key in nonleaders:
# 		nonleaders[key].setColor('blue')

def mis_violation_check(nodelist):
	nonVisited = 0
	bothInL = 0
	noRedNeighbour = 0

	for node in nodelist:
		if node.color == 'yellow':
			nonVisited += 1

		if node.color == 'red': 
			for neighbour in node.edges:
				if neighbour.color == 'red':
					bothInL += 1

		if node.color == 'blue':
			flag = False
			for neighbour in node.edges:

				if neighbour.color == 'red':
					flag = True

			if not flag:
				noRedNeighbour += 1

	# Double edges
	bothInL = bothInL / 2


	print '\n\nNode not in L or NL \t\t', nonVisited
	print 'Two adjacent nodes both in L\t', bothInL
	print 'No neighbour in L\t\t', noRedNeighbour
	# print '\n\nViolations:', (nonVisited+bothInL+noRedNeighbour)
	return nonVisited+bothInL+noRedNeighbour


def vc_violation_check(nodelist):
	tally = 0
	for node in nodelist:
		for neighbour in node.edges:
			if node.color == neighbour.color:
				tally += 1
		if node.color == 'yellow':
			tally += 2

	# Double edges
	tally = tally / 2
	print '\n\nViolations\t\t', tally