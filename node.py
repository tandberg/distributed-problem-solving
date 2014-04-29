from random import randint, random
from copy import copy

class Node(object):
	def __init__(self, index, x=0, y=0, edges=None, color='black'):
		self.index = index
		self.y = y
		self.x = x
		self.edges = []
		self.color = color
		self.messages = []
		self.pendingMsgs = []
		self.state = 0
		self.tmpColor = None

	def setColor(self, color):
		self.color = color

	def setState(self, state):
		self.state = state

	def addMessage(self, message):
		self.messages.append(message)

	def broadcastMIS(self, message):
		for node in self.edges:
			node.addMessage(message)

	def broadcastVC(self, message):
		self.pendingMsgs.append(message)


	def reciveceMsg(self, message):
		if message['intend'] == self.tmpColor:
			self.tmpColor = None

	def sendMsgs(self):
		for node in self.edges:
			for msg in self.pendingMsgs:
				node.reciveceMsg(msg)

		self.pendingMsgs = [] # empty the pool

	def __str__(self):
		return '{0} - [-{1}-] - {2}\n'.format(self.index, self.color, self.available_colors) #self.index, ', '.join(str(x.index) for x in self.edges))

	def __repr__(self):
		return self.__str__()

	def addedge(self, node):
		self.edges.append(node)

	def resetMessages(self):
		self.messages = []

	def setColorOptions(self, color_options):
		self.color_options = color_options
		self.available_colors = color_options

	def randomAvailableColor(self):
		cols = copy(self.color_options.values())
		for neighbour in self.edges:
			if neighbour.color in cols:
				cols.remove(neighbour.color)

		if len(cols) == 0:
			self.tmpColor = None
			# self.edges[randint(0, len(self.edges)-1)].setColor('black')
		else:
			self.tmpColor = cols[randint(0, len(cols)-1)]
		self.available_colors = cols


	def maybeRandomUncolor(self):
		for node in self.edges:
			if len(node.available_colors) == 0:
				if random() > 0.5:
					self.setColor('black')







