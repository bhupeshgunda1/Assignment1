def main():
    routes()


def routes():
    # add edges as list with weight
    edges = [['A', 'B', 5], ['B', 'C', 4], ['C', 'D', 8], ['D', 'C', 8], ['D', 'E', 6], ['A', 'D', 5], ['C', 'E', 2],
             ['E', 'B', 3], ['A', 'E', 7]]
    route = ['A', 'D', 'C']
    distance = 0  # initialize distance to 0
    routestops = 0  # initialize number of stops to 0
    sourceNode = route[routestops]
    destNode = route[routestops + 1]
    # Code to find the distance between the nodes
    for i in edges:
        for edge in edges:
            if edge[0] is sourceNode:
                if edge[1] is destNode:
                    distance = distance + edge[2]
                    routestops = routestops + 1
                    print("sourceNode: " + str(sourceNode))
                    print("destNode: " + str(destNode))
                    print(f"distance between {sourceNode} and {destNode} is : " + str(distance))
                    print(f"The number of stops for the route(A,D,C) is {routestops}")
                    sourceNode = route[routestops]
                    if routestops < 2:
                        destNode = route[routestops + 1]
                    if destNode is route[len(route) - 1]:
                        break


main()