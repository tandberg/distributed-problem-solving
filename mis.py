from random import random
import helper
import math

class MinimalIndependentSet:
	def __init__(self, nodelist, M):
		d = helper.maxEdges(nodelist)
		self.algorithm(nodelist, d, M)
		helper.mis_violation_check(nodelist)

	def algorithm(self, nodelist, d, M):
		p = 1.0/d
		N = len(nodelist)

		while(p <= 1):
			for i in xrange(int(M * math.log(N, 2))):

				loners = filter((lambda x: x.color == 'black'), nodelist)
				# Round 1
				msg = 'r1_{0}'.format(i)
				for node in loners: 
					if p >= random():
						node.broadcastMIS(msg)
						node.setState(1)

				for node in loners:
					if msg in node.messages:
						node.setState(0)

				# Round 2
				msg = 'r2_{0}'.format(i)
				for node in loners:
					if node.state == 1:
						node.setColor('red')
						node.broadcastMIS(msg)

				loners = filter((lambda x: x.color == 'black'), nodelist)
				for node in loners:
					if msg in node.messages:
						node.setColor('blue')

				for node in loners:
					node.resetMessages()

			p *= 2

