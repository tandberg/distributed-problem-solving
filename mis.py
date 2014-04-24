from random import random
import helper
import math


def MinimalIndependentSet(nodelist, M):
	d = helper.maxEdges(nodelist)
	results = mis(nodelist, d, M)

def mis(nodelist, d, M):
	p = 1.0/d
	N = len(nodelist)

	while(p <= 1):
		loners = filter((lambda x: x.color == 'yellow'), nodelist)
		for i in xrange(int(M * math.log(N))):
			# Round 1
			msg = 'r1_{0}'.format(i)
			for node in loners:
				if p > random():
					node.broadcast(msg)
					node.setState(1)

			for node in loners:
				if node.message == msg:
					node.setState(0)

			# Round 2
			msg = 'r2_{0}'.format(i)
			for node in loners:
				if node.state == 1:
					node.setColor('red')
					node.broadcast(msg)

			for node in loners:
				if node.message == msg:
					node.setColor('blue')
		print loners
		p *= 2
