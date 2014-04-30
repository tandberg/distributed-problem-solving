from random import random
import helper
import math

COLORPALETTE = {
	0: 'red',
	1: 'blue',
	2: 'green',
	3: 'yellow',
	4: 'pink',
	5: 'orange',
	6: 'purple',
	7: 'teal',
	8: 'darkgreen',
	9: 'greenyellow'
}

class VertexColoring:
	def __init__(self, nodelist, M, K):
		d = helper.maxEdges(nodelist)

		self.algorithm(nodelist, d, M, K)
		helper.vc_violation_check(nodelist)

	def algorithm(self, nodelist, d, M, K):
		p = 1.0/d
		N = len(nodelist)

		colors = {}
		for i in range(K):
			colors[i] = COLORPALETTE[i]

		for node in nodelist:
			node.setColorOptions(colors)

		while(p <= 1):
			for i in xrange(int(M * math.log(N, 2))):

				for node in nodelist:
					node.maybeRandomUncolor()

				loners = filter(lambda x: x.color == 'black', nodelist)

				# Round 1
				for node in loners:
					msg = {}
					if p >= random():
						node.randomAvailableColor()
						msg['intend'] = node.tmpColor
						node.broadcastVC(msg)

				for node in loners:
					node.sendMsgs()

				# Round 2
				for node in loners:
					msg = {}
					if node.tmpColor != None:
						node.setColor(node.tmpColor)

				for node in loners:
					node.resetMessages()


			p *= 2


