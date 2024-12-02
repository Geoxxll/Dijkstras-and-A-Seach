import heapq


def dijsktraSearch(startNode, goalNode, myMap):
    resList = []
    openList = []
    closeList = {}

    heapq.heappush(openList, startNode)
    closeList[startNode.state_hash()] = startNode

    while (len(openList) != 0):
        current = heapq.heappop(openList)
        if (current == goalNode):
            resList = [current.get_cost(), len(closeList), closeList]
            return resList
        currentChildren = myMap.successors(current)
        
        for child in currentChildren:
            childHashKey = child.state_hash()
            if (childHashKey not in closeList):
                child.set_cost(child.get_g())
                heapq.heappush(openList, child)
                closeList[childHashKey] = child
            if (childHashKey in closeList and child.get_g() < closeList[childHashKey].get_cost()):
                child.set_cost(child.get_g())
                closeList[childHashKey] = child
                heapq.heappush(openList, child)

    return [-1, len(closeList), closeList]


        

