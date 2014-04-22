class Node:
	def __init__(self, index, x=0, y=0, edges=None, color='black'):
		self.index = index
		self.y = y
		self.x = x
		self.edges = []

	def setColor(self, color):
		self.color = color

	def setState(self, state):
		self.state = state

	def broadcast(self, message):
		for i in self.edges:
			print 'Send message to ' + self.edges[i]

	def __str__(self):
		return '{0} - [{1}]'.format(self.index, ', '.join(str(x.index) for x in self.edges))

	def __repr__(self):
		return self.__str__()

	def addedge(self, node):
		self.edges.append(node)


# n = Node("1:2, 3:21", 'blaa', 'asd')

# n.setColor('yellow')
# print n


# liste = range(3)

# for i in liste:
# 	liste[i] = Node('hei', 'red')

# print liste