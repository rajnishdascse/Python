class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
        
def pre_order(root):
    if root:
        print(root.data, end=' ')
        pre_order(root.left)
        pre_order(root.right)
        
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end =' ')
        
        
root = Node(2)
root.left = Node(1)
root.right = Node(9)
root.right.left = Node(4)
root.right.right = Node(12)
root.right.right.right = Node(44)

print('Inorder Traversal elements are: ')
inorder(root)

print('\nPreorder Traversal elements are: ')
pre_order(root)
print('\nPostorder Traversal elements are: ')
post_order(root)

    