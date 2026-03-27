class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum_number(self):
        return self.a+ self.b
    
a = A(5,3)
ans = a.sum_number()
print(ans)