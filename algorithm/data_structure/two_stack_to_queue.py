#如何用两个栈实现队列

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def stack2ToStack1(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())

def push(self, number):
    self.stack2.append(number)
    
    def pop(self):
        if not self.stack1:
            self.stack2ToStack1()
        return self.stack1.pop()
    
    def top(self):
        if not self.stack1:
            self.stack2ToStack1()
        return self.stack1[-1]
