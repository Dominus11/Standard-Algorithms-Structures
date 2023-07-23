# Stack

class StackOverFlow(Exception):
    def __init__(self):
        Exception.__init__(self, "Stack limit has been exceeded. Please remove items from your stack before adding any more.")

class Frame:
    def __init__(self, dataValue, nextFrame = None, prevFrame = None):
        self.value = dataValue
        self.next = nextFrame
        self.prev = prevFrame

    __str__ = lambda self: f"Value: {self.value} \nNext Frame: {self.next.getValue() if self.next != None else None} \nPrevious Frame: {self.prev.getValue() if self.prev != None else None}"
    getNextFrame = lambda self: self.next
    getPrevFrame = lambda self: self.prev
    getValue = lambda self: self.value

    def setPrevFrame(self, frame): 
        self.prev = frame
    
    def setNextFrame(self, frame):
        self.next = frame

class Stack:
    def __init__(self, maxLength = 1000, *dataValues):
        self.maxLength = maxLength
        self.length = 0
        self.topFrame = None

        frames = [Frame(dataValues[i]) if type(dataValues[i]) != Frame else dataValues[i] for i in range(len(dataValues))]
        for i in range(len(frames)):
            if i > 0: frames[i].setPrevFrame(frames[i-1]) 
            if i < len(frames) -1 : frames[i].setNextFrame(frames[i+1])
            self.push(frames[i])
        
        del frames

    isEmpty = lambda self: self.length == 0
    isFull = lambda self: self.length == self.maxLength
    peek = lambda self: self.topFrame

    # push
    def push(self, frame: Frame):
        if self.isFull():
            raise StackOverFlow

        if self.isEmpty():
            self.topFrame = frame
            self.length += 1
            return

        frame.setPrevFrame(self.topFrame)
        self.topFrame.setNextFrame(frame)
        self.topFrame = frame
        self.length += 1
    
    # pull
    def pull(self):
        temp = self.topFrame
        self.topFrame = temp.prev
        self.topFrame.setNextFrame(None)
        return temp
    
    # getStack - Generator of the stack items, with the lowest stack items at the end of the generator
    def getStack(self):
        current = self.peek()

        while current != None:
            yield current
            current = current.getPrevFrame()

def main():
    print("Creating Stack")
    stack = Stack(1000, *[Frame(i) for i in range(20)])
    print([frame.getValue() for frame in stack.getStack()])
    print("\nPushing to Stack")
    stack.push(Frame(20, prevFrame = stack.peek()))
    print(stack.peek())
    print("\nPulling from Stack")
    stack.pull()
    print(stack.peek())

if __name__ == "__main__":
    main()