# Linked Lists

class Node:
    def __init__(self, value, idx = 0, prevNode = None, nextNode = None ):
        self.dataField = value
        self.prev = prevNode
        self.next = nextNode
        self.idx = idx
    
    __str__ = lambda self: f'Datafield: {self.dataField} \nNext Node: {self.next.dataField if self.next != None else None} \nPrevious Node: {self.prev.dataField if self.prev != None else None} \nIndex: {self.idx}\n\n'        
    getNextNode = lambda self: self.next
    getPrevNode = lambda self: self.prev
    getDataField = lambda self: self.dataField

    def setNextNode(self, nextNode):
        self.next = nextNode
    
    def setPrevNode(self, prevNode):
        self.prev = prevNode

    def setDataField(self, value):
        self.dataField = value 
    
    def setIdx(self, idx: int):
        self.idx = idx
    
class LinkedList:
    def __init__(self, *dataValues):
        self.head = None
        self.tail = None
        self.length = 0

        # Issue: Composition rather than Aggregation, best case would be to create nodes outside of linked-list
        nodes = [Node(value = dataValues[i], idx = i) if type(dataValues[i]) != Node else dataValues[i] for i in range(len(dataValues)) ]
        
        # Set up the links if they're not there already
        for i in range(len(nodes)):
            if nodes[i].getNextNode() != None: break
            if i < len(nodes) - 1: nodes[i].setNextNode(nodes[i+1])
            if i > 0: nodes[i].setPrevNode(nodes[i-1])
            self.append(nodes[i])
        
        del nodes
        

    __str__ = lambda self: "Empty Linked List" if self.isEmpty() else f'Linked List: [{ ",".join([str(node.getDataField()) for node in self.traverse()]) }]'
    __len__ = lambda self: self.length
    getHead = lambda self: self.head
    getTail = lambda self: self.tail
    getLinkedList = lambda self: [node.getDataField() for node in self.traverseRec()]
    isEmpty = lambda self: self.head == None
   
    # setHead - Set a new head for the linkedlist
    def setHead(self, newHead: Node):
        newHead.setNextNode(self.head)
        self.head = newHead  
        for node in self.traverse(): node.idx += 1

    # append - Add a new tail
    def append(self, node: Node):
        if self.isEmpty():
            self.head = node
        else:
            node.setIdx(self.length)
            node.setPrevNode(self.tail)
            self.tail.setNextNode(node)
        
        self.tail = node
        self.length += 1

    # traverse - Generator of the items in the Linked-List 
    def traverse(self):
        current = self.getHead()

        while current != self.tail: 
            yield current
            current = current.getNextNode()
        else:
            yield self.tail

    # traverseRec - Recursive generator of the items in the Linked-List
    def traverseRec(self, current = "Head"):
        current = self.getHead() if current == "Head" else current

        if current == self.getTail():
            yield current
            return

        yield current
        yield from self.traverseRec(current = current.getNextNode())

    # search - Linear Search for a node with a target value
    def search(self, nodeValue):
        for node in self.traverse():
            if nodeValue == node.dataField:
                return node
    
    # getNodeAt - Gets the node at a given index
    def getNodeAt(self, idx):
        if idx > self.length or idx < 0:
            return None
        
        for node in self.traverse():
            if node.idx == idx:
                return node

        return None

    # insert - Insert an item at a given position
    def insert(self, newNode: Node, idx: int):
        # Edge Cases: 
        #   Adding a new head
        #   Empty LinkedList
        #   Index greater than length of LinkedList
        #   Index < 0

        if self.isEmpty() or idx < 0:
            self.setHead(newNode)
            return
        
        if idx >= self.length:
            self.append(newNode)
            return

        if idx == 0:
            self.setHead(newNode)
            return

        newNode.idx = idx
        for node in self.traverse():
            if node == newNode: continue
            if node.idx == idx - 1:
                # 1. Set the previous pointer of the item that will come after the node being inserted to newNode
                node.getNextNode().setPrevNode(newNode)
                # 2. Set the new node's previous node to the node which we desire to be previous
                newNode.setPrevNode(node)
                # 3. Set the new node's next node to be the node which we desire to be afterwards
                newNode.setNextNode(node.getNextNode())
                # 4. Set the previous node's next node to be newNode
                node.setNextNode(newNode)
            
            # Indexing housework
            if node.idx >= idx:
                node.idx += 1
        
        self.length += 1

    # update - Update the datafield of a node at a given index
    def update(self, newVal, idx: int):
        if idx < 0 or idx >= self.length:
            raise ValueError

        for node in self.traverse():
            if node.idx == idx:
                node.setDataField(newVal)
                break

    # remove - Remove an item from a given position
    def remove(self, idx: int):
        if idx >= self.length:
            return    

        for node in self.traverse():

            if node.idx == idx - 1:
                # Change the pointer of the item after the one being removed
                nextNode = node.getNextNode() 
                if nextNode.getNextNode() == None: break
                nextNode.getNextNode().setPrevNode(node)
                # Change the pointer of the item before the one being removed
                node.setNextNode(node.next.next)

            if node.idx > idx:
                node.idx -= 1
        
        self.length -= 1


def main():
    # All of this works!
    linkedList = LinkedList(5,1,3)

    for node in linkedList.traverse():
        print(node)
    
    print("Testing Removal")
    linkedList.remove(1)
    print(linkedList.getHead())
    
    print("Testing Insertion")
    linkedList.insert(Node(1), 1)
    print(linkedList.getHead())
    print(linkedList.getTail())

    print("Testing Modification")
    linkedList.update(2,1)
    print(linkedList.getNodeAt(1))

    print([node.getDataField() for node in linkedList.traverse()])
    

if __name__ == "__main__":
    main()
