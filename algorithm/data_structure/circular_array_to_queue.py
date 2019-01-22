"""
http://www.lintcode.com/zh-cn/problem/implement-queue-by-circular-array/
"""

class CircularQueue:
    def __init__(self, n):
        self.circularArray = [0]*n
        self.front = 0
        self.rear = 0
        self.size = 0
    
    """
        @return:  return true if the array is full
        """
    def isFull(self):
        return self.size == len(self.circularArray)
    
    """
        @return: return true if there is no element in the array
        """
    def isEmpty(self):
        return self.size == 0
    
    """
        @param element: the element given to be added
        @return: nothing
        """
    def enqueue(self, element):
        if self.isFull():
            raise RuntimeError("Queue is already full")
        self.rear = (self.front+self.size) % len(self.circularArray)
        self.circularArray[self.rear] = element
        self.size += 1
    
    """
        @return: pop an element from the queue
        """
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Queue is already empty")
        ele = self.circularArray[self.front]
        self.front = (self.front+1) % len(self.circularArray)
        self.size -= 1
        return ele

