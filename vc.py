import helper

COLORPALETTE = {
	0: 'red',
	1: 'blue',
	2: 'green',
	3: 'teal',
	4: 'pink',
	5: 'orange',
	6: 'purple',
	7: 'yellow',
	8: 'darkgreen',
	9: 'greenyellow'
}

def VertexColoring(nodelist, K):
	print 'VertexColoring', K
	vc(nodelist, K, helper.maxEdges(nodelist))

def vc(nodelist, K, d):
	p = 1.0/d

	colors = {}
	for i in range(K):
		colors[i] = COLORPALETTE[i]

	for node in nodelist:
		node.color_options = K

	while(True):
		if p >= 1:
			break

		# Round 1
		for node in nodelist:
			c = colors[int(random()*len(colors))]

			if p > random():
				node.broadcast(c)
				c.setColor(c)

			if node.message == c:
				exit

		# Round 2
		for node in nodelist:
			exit
