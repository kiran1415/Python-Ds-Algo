class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




root = Node(5)
node2 = Node(6)
node3 = Node(7)

root.left = node2
root.right = node3
