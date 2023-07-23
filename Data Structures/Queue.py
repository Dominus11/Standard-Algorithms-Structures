# Queue

# Node - Implementation of a node on a queue
class Node:
    def __init__(self, value = None, idx: int = None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        self.priority = None
        self.idx = idx
    
    __str__ = lambda self: f'Value {self.value} \nNext Node: {self.nextNode.getValue() if self.nextNode != None else None}'
    getValue = lambda self: self.value
    getNextNode = lambda self: self.nextNode

    def setValue(self, value):
        self.value = value
    
    def setNextNode(self, node):
        self.nextNode = node

# Queue- FIFO data structure.
class Queue:
    def __init__(self, maxLength = 1000, *dataValues):
        self.front = None
        self.back = None
        self.maxLength = maxLength
        self.length = 0

        elements = [Node(value = dataValues[i], idx = None) if type(dataValues[i]) != Node else dataValues[i] for i in range(len(dataValues))]

        for i in range(len(elements)):
            if i < len(elements) - 1: elements[i].setNextNode(elements[i+1])
            self.enqueue(elements[i])

        del elements

    peek = lambda self: self.front
    isEmpty = lambda self: self.length == 0
    isFull = lambda self: self.length == self.maxLength

    # enqueue
    def enqueue(self, newNode):
        if self.isFull(): return "Queue Overflow"

        if self.isEmpty(): 
            self.front = self.back = newNode
            self.length += 1
            return
        
        self.back.setNextNode(newNode)
        self.back = newNode
        self.length += 1
    
    # dequeue
    def dequeue(self):
        self.front = self.front.getNextNode()
        self.length -= 1

    # getQueue - Generator of the items in the queue
    def getQueue(self):
        current = self.front

        while current != None:
            yield current
            current = current.getNextNode()

def main():
    print("Creating Queue")
    queue = Queue(1000, *[Node(i) for i in range(20)])
    print([node.getValue() for node in queue.getQueue()])
    print("\nEnqueue")
    queue.enqueue(Node(20, idx = queue.length - 1))
    print(queue.back)
    print("\nDequeue")
    queue.dequeue()
    print(queue.peek())

if __name__ == "__main__":
    main()