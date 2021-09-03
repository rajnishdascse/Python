class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def print_root(root):
    current = root
    stack =[]

    
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
            
        elif(stack):
            current=stack.pop()
            print(current.data, end=' ')
            current = current.right
        else:
            break
    print()

root = Node(2)
root.left = Node(1)
root.right = Node(9)
root.right.left = Node(4)
root.right.right = Node(12)
root.right.right.right = Node(44)
print_root(root)