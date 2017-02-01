#!/usr/bin/python

from collections import defaultdict, deque

def getNodeToEdgeMap(filename):
    '''
    Returns a map of {node_name: edge_list}
    where edge_list is a list of (other_node_name, is_border) 2-tuples
    '''
    nodeToEdgeMap = defaultdict(list)
    for line in open(filename, 'r').xreadlines():
        if line: # Skip empty last line
            ls = line.split(',')
            nodeToEdgeMap[ls[0]].append((ls[1], int(ls[2])))
            nodeToEdgeMap[ls[1]].append((ls[0], int(ls[2])))
    return nodeToEdgeMap

def getRegion(nodeToEdgeMap):
    '''
    Peels the first node (by key, could be in any order)
    out of nodeToEdgeMap and returns a list of all nodes
    in the same region. nodeToEdgeMap is modified so all
    nodes in the same region are removed before return.
    '''
    thisRegion, nodeQueue = set(), deque()
    nodeQueue.append(next(nodeToEdgeMap.iterkeys()))

    while nodeQueue:
        nodeKey = nodeQueue.popleft()
        node = nodeToEdgeMap.pop(nodeKey)
        thisRegion.add(nodeKey)

        for otherNode, isBorder in node:
            if not isBorder and otherNode not in thisRegion:
                thisRegion.add(otherNode)
                nodeQueue.append(otherNode)

    return list(thisRegion)

def main():
    nodeToEdgeMap, regions = getNodeToEdgeMap('data.csv'), []

    while nodeToEdgeMap:
        regions.append(getRegion(nodeToEdgeMap))

    for region in regions:
        print(region)

if __name__ == '__main__':
    main()

'''
Sample data for data.csv:

Askersund,Borlange,0
Askersund,Copenhagen,1
Askersund,Dallerup,1
Borlange,Dallerup,1
Copenhagen,Dallerup,0

'''