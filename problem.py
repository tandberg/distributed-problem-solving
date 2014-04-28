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

def main(algorithm='vc', file='simple', K=3, M=50):
	# Readings
	readinput(file)

	# Algorithms and violationresults
	if algorithm == 'vc':
		VertexColoring(nodelist, K)
		vc_violation_check(nodelist)
	else:
		MinimalIndependentSet(nodelist, M)

	# Print to screen
	draw_graph(nodelist)

if __name__ == '__main__':
	# try:
		if sys.argv[0] == 'vc':
			main(algorithm=sys.argv[1], file=sys.argv[2], M=int(sys.argv[3]), K=int(sys.argv[4]))
		elif sys.argv[1] == 'mis':
			main(algorithm=sys.argv[1], file=sys.argv[2], M=int(sys.argv[3]))
	# except Exception:
	# 	print 'Usage:\n\npython problem.py mis file M\n\n\t or\n\npython problem.py vc file M K'




