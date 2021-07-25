class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        self.stack.pop()
    
    def peek(self):
        print(self.stack[len(self.stack)-1])

    
    def size(self):
        print(len(self.stack))
    def print_stack(self):
        ans = []
        for i in range(len(self.stack)):
            ans.append(str(self.stack[i]))
        print(','.join(ans))




p1 = Stack()

p1.push(5)
p1.push(4)
p1.push(52)
p1.push(41)
p1.push(3)
p1.push(9)
p1.print_stack()
p1.peek()
p1.size()
p1.pop()
p1.size()
p1.peek()
p1.print_stack()