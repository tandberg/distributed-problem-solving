
import sys
from node import Node
from printing import draw_graph
from mis import MinimalIndependentSet
from vc import VertexColoring
from helper import mis_violation_check, vc_violation_check

# GLOBALS
nodelist = []

def readinput(inputfile='simple'):
	fil = open('input/{0}.txt'.format(inputfile), 'r')
	first = fil.readline()
	nodes = int(first.split(' ')[0])
	edges = int(first.split(' ')[1])
	print "Nodes:", nodes, "Edges:", edges

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



def main(algorithm='vc', K=3):
	# Readings
	readinput('graph-color-1')
	# readinput('spiral-500-4-color1')

	# Algorithms and violationresults
	if algorithm == 'vc':
		VertexColoring(nodelist, K)
		vc_violation_check(nodelist)
	else:
		MinimalIndependentSet(nodelist)
		mis_violation_check(nodelist)

	# Print to screen
	draw_graph(nodelist)

if __name__ == '__main__':
	if len(sys.argv) > 2:
		main(sys.argv[1], sys.argv[2])
	else:
		main('mis')