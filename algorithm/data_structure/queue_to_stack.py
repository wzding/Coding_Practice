#如何用两个队列实现一个栈？
from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    # 将queue1中元素移入queue2,留下最后一个。
    def moveItems(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

def swapQueues(self):
    self.queue1, self.queue2 = self.queue2, self.queue1
    
    def push(self, x):
        self.queue1.append(x)
    
    def pop(self):
        self.moveItems()
        self.queue1.popleft()
        self.swapQueues()
    
    def top(self):
        self.moveItems()
        item = self.queue1.popleft()
        self.swapQueues()
        self.queue1.append(item)
        return item
    
    def isEmpty(self):
        return len(self.queue1) == 0
