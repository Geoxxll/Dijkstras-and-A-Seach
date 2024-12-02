import heapq

def aStarSearch(start, goal, myMap):
    resList = []
    openList = []
    closeList = {}

    start.set_cost(get_h(start, goal))
    heapq.heappush(openList, start)
    closeList[start.state_hash()] = start

    while (len(openList) != 0):
        current = heapq.heappop(openList)
        if (current == goal):
            resList = [current.get_cost(), len(closeList), closeList]
            return resList
        curChildren = myMap.successors(current)

        for child in curChildren:
            childHashKey = child.state_hash()
            child_h_value = get_h(child, goal)
            if (childHashKey not in closeList):
                child.set_cost(child.get_g() + child_h_value)
                heapq.heappush(openList, child)
                closeList[childHashKey] = child
            if (childHashKey in closeList and child.get_g() + child_h_value < closeList[childHashKey].get_cost()):
                # del closeList[childHashKey]
                child.set_cost(child.get_g() + child_h_value)
                # closeList[childHashKey].set_cost(child.get_g() + child_h_value)
                closeList[childHashKey] = child
                heapq.heappush(openList, child)

    return [-1, len(closeList), closeList]



def get_h(cur, goal):
    delta_x = abs(cur.get_x() - goal.get_x())
    delta_y = abs(cur.get_y() - goal.get_y())

    result = 1.5 * min(delta_x, delta_y) + abs(delta_x - delta_y)
    return result

def helper(cx, cy, gx, gy):
    return 1.5 * min(abs(cx - gx), abs(cy - gy)) + abs(abs(cx - gx) - abs(cy - gy))
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
       print(helper(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
    else:
        print("Please provide cur and goal.")