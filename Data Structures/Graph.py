# Graph

class Node:
    def __init__(self, value, *edges):
        self.value = value
        self.edges = {}
        self.addEdge(*edges)

    __str__ = lambda self: f'Node value: {self.value}'# \nNext Nodes: {[node for node in self.edges]}'
    __repr__ = lambda self: f'<NodeObject>: Value {self.value}'#/ Edges {self.getNeighbours()}'
    hasNeighbours = lambda self: len(self.edges) > 0
    getNeighbours = lambda self: list(self.edges.keys())
    isConnectedTo = lambda self, targetNode: targetNode in self.edges 

    def addEdge(self, *edges):
        for edge in edges:
            if len(edge) == 1: self.edges[edge[0]] = None
            if len(edge) == 2: self.edges[edge[0]] = edge[1]
    
    def removeEdge(self, targetNode):
        if self.isConnectedTo(targetNode):
            del self.edges[targetNode]

    def __del__(self):
        # Can be optional to change. Perhaps return the node info instead?
        print(str(self))
        print(f"{self.value} has been deleted.\n\n\n")

class Graph:
    def __init__(self, adjacencyList: dict):
        self.nodes = dict()

        for nodeVal, edges in adjacencyList.items():
            self.nodes[nodeVal] = Node(nodeVal, *edges)

    def __str__(self): 
        out = ""
        for nodeVal, node in list(self.nodes.items()): out += str(node) + "\n\n"
        return out


    def addNode(self, *nodes: Node): 
        for targetNode in nodes:
            self.nodes[targetNode.value] = targetNode

    def removeNode(self, targetNode):
        for nodeVal, node in self.nodes.items():
            if node.isConnectedTo(targetNode): del node.edges[targetNode]
        
        del self.nodes[targetNode]
        

     # Note: Graphs tend to only have BFS and DFS, Trees can have inOrder and postOrder, but for sake of ease I shall make these tree exclusive algorithms.
     # It is possible to give a graph an in-order and post-order traversal but that is unsuitable in this case.
    def BFS(self, startNode : Node = None):
        startNode = self.nodes[startNode] if startNode != None else list(self.nodes.values())[0]
        nodeQueue = [startNode]
        visited = []

        while len(nodeQueue) > 0:
            currentNode = nodeQueue.pop(0)
            yield currentNode
            visited.append(currentNode)

            if not currentNode.hasNeighbours(): continue
            for nodeVal in currentNode.getNeighbours():
                node = self.nodes[nodeVal]
                if not node in visited and node not in nodeQueue: nodeQueue.append(node)
        
        return

    # In this case it is preorder
    def DFS(self, startNode: Node = None):
        startNode = self.nodes[startNode] if startNode != None else list(self.nodes.values())[0]
        nodeStack = [startNode]
        visited = []

        while len(nodeStack) > 0:
            currentNode = nodeStack.pop()
            yield currentNode
            visited.append(currentNode)
            
            for edge in currentNode.getNeighbours()[::-1]:
                node = self.nodes[edge[0]]
                if not (node in visited or node in nodeStack):
                    nodeStack.append(node)

        return
    
def main():
    adjacencyList = {'A': [('B',5), ('C', 6), ('E', 7)],
                     'B': [ ('A', 5), ('C', 3), ('F', 2)],
                     'C': [ ('A', 6), ('B', 3), ('D', 4)],
                     'D': [ ('C', 4) ,('E', 3) ],
                     'E': [('A', 7), ('D', 3)], 
                     'F': [('B', 2)],
                     }
    graph = Graph(adjacencyList)
    print('Graph made')
    print(graph)
    print('Adding nodes G and H')
    nodeG = Node('G', ('H', 2))
    nodeH = Node('H', ('G', 2))
    graph.addNode(nodeG, nodeH)
    print('Removing node H')
    graph.removeNode('H')
    print(graph.nodes['G'])
    print("BFS")
    print([node for node in graph.BFS('B')])
    print("\n\n DFS")
    print([node for node in graph.DFS('B')])


if __name__ == "__main__":
    main()
