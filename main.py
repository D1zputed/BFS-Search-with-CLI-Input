from collections import deque

def bfs_path(graph, start, goal):
    # If start and goal are the same node, return the single node path
    if start == goal:
        return [start]
    
    # A queue to manage the frontier of exploration (stores paths, not nodes)
    queue = deque([[start]])
    
    # A set to store visited nodes to avoid cycles
    visited = set([start])
    
    while queue:
        # Get the next path from the queue
        path = queue.popleft()
        node = path[-1]
        
        # Explore all neighbors of the current node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                # Construct a new path to this neighbor
                new_path = list(path)
                new_path.append(neighbor)
                
                # If we reached the goal, return the path
                if neighbor == goal:
                    return new_path
                
                # Otherwise, add the new path to the queue for further exploration
                queue.append(new_path)
                visited.add(neighbor)
    
    # If we exhaust the queue and never reach the goal, return None
    return None

def getNumNodes() -> int:
    nodeNumber = 0
    while(True):
        try:
            nodeNumber = int(input("How many nodes do you want?(Maximum 26)"))
            if nodeNumber <= 0 or nodeNumber > 26:
                print("Number not within range")
            else:
                return nodeNumber
        except ValueError:
            print("Must be a number")

def setNodes(amount: int) -> list[str]:
    alpabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cutAlpabeth = alpabeth[0:amount]
    return list(cutAlpabeth)

def setLinks(nodes: list[str]) -> dict:
    print("-------------------")
    print("Set the adjacency list")
    print("-------------------")
    usedLetters = ["A"]
    graph = {}
    for letter in nodes:
        while(True):
            neighbors = input(f"Enter neighbors for node {letter}(separate by comma only):").upper()
            if neighbors:
                neighbors = neighbors.split(",")
                test = set(neighbors).issubset(nodes) and not bool(set(neighbors) & set(usedLetters))
            else:
                neighbors = []
            if test:
                usedLetters.extend(neighbors)
                graph[letter] = neighbors
                break
            else:
                print("Wrong input")

    return graph

def askStartEnd(nodes: list[str]) -> tuple:
    while(True):
        print("------------------------")
        start = str(input("What node should it start?"))
        end = str(input("What node Should it end?"))
        if start in nodes and end in nodes:
            break
        else:
            print("Input not in list of nodes")
    return start, end
    

def main():
    nodeNumber = getNumNodes()
    nodes = setNodes(nodeNumber)
    print(f"the nodes are {nodes}")
    
    graph = setLinks(nodes)
    start, end = askStartEnd(nodes)

    path = bfs_path(graph, start, end)

    if path:
        print("Path found:", path)
    else:
        print("No path found")
        
main()

