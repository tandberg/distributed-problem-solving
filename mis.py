from random import random
import helper


def MinimalIndependentSet(nodelist):
	d = helper.maxEdges(nodelist)
	results = mis(d, nodelist)

def mis(d, nodelist):
	p = 1.0/d

	iteration = 1
	while(True):
		if p >= 1:
			break

		# Round 1
		for node in nodelist:
			if node.color == 'yellow':
				msg = 'msg_r1_{0}'.format(iteration)

				if p > random():
					node.broadcast(msg)
					node.setState(1)

				if node.message == msg:
					node.setState(0)

		# Round 2
		for node in nodelist:
			if node.color == 'yellow':
				msg = 'msg_r2_{0}'.format(iteration)

				if node.state == 1:
					node.setColor('red')
					node.broadcast(msg)

				if node.message == msg:
					node.setColor('blue')


		p = 2*p
		iteration += 1
