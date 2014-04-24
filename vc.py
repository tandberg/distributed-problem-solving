import helper

COLORPALETTE = {
	0: 'red',
	1: 'blue',
	2: 'green',
	3: 'teal',
	4: 'pink',
	5: 'orange',
	6: 'purple',
	7: 'black',
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




# def MinimalIndependentSet(nodelist):
# 	d = helper.maxEdges(nodelist)
# 	results = mis(d, nodelist)

# def mis(d, nodelist):
# 	p = 1.0/d

# 	iteration = 1
# 	while(True):
# 		if p >= 1:
# 			break

# 		# Round 1
# 		for node in nodelist:
# 			if node.color == 'yellow':
# 				msg = 'msg_r1_{0}'.format(iteration)

# 				if p > random():
# 					node.broadcast(msg)
# 					node.setState(1)

# 				if node.message == msg:
# 					node.setState(0)

# 		# Round 2
# 		for node in nodelist:
# 			if node.color == 'yellow':
# 				msg = 'msg_r2_{0}'.format(iteration)

# 				if node.state == 1:
# 					node.setColor('red')
# 					node.broadcast(msg)

# 				if node.message == msg:
# 					node.setColor('blue')


# 		p = 2*p
# 		iteration += 1