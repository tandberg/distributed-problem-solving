class Node:
	def __init__(self, index, x=0, y=0, edges=None, color='yellow'):
		self.index = index
		self.y = y
		self.x = x
		self.edges = []
		self.color = color
		self.message = ''
		self.state = -1
		self.color_options = {}

	def setColor(self, color):
		self.color = color

	def setState(self, state):
		self.state = state

	def setMessage(self, message):
		self.message = message

	def broadcast(self, message):
		for node in self.edges:
			node.setMessage(message)

	def __str__(self):
		return '{0} - [{1}]'.format(self.index, ', '.join(str(x.index) for x in self.edges))

	def __repr__(self):
		return self.__str__()

	def addedge(self, node):
		self.edges.append(node)

