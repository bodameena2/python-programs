class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(30)
root.left.right = Node(50)

preorder(root)
