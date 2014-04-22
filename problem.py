# from helper import Helper, Lol
from node import Node

# class Problem:
# 	def __init__(self, ein, to):
# 		print 'init#Problem', ein, to





# # problem = Problem(2,3)
# # helper = Helper()
# # helper = Helper()
# # lol = Lol()
# # lolaa = Lol()

# for i in xrange(10):
# 	print i


fil = open('input/simple.txt', 'r')
first = fil.readline()
nodes = int(first.split(' ')[0])
edges = int(first.split(' ')[1])
print "Nodes:", nodes, "Edges:", edges


nodelist = []
for i in range(nodes):
	line = fil.readline()
	node = Node(int(line.split(' ')[0]), float(line.split(' ')[1]), float(line.split(' ')[2]))
	nodelist.append(node)

for i in range(edges):
	line = fil.readline()
	node1 = nodelist[int(line.split(' ')[0])]
	node2 = nodelist[int(line.split(' ')[1])]

	node1.addedge(node2)
	node2.addedge(node1)

print nodelist
