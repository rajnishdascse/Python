class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)
                
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)
    
    def inorder_traverse(self):
        elements =[]
        if self.left:
            elements += self.left.inorder_traverse()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traverse()
        return elements
        
        
    def preorder_traverse(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traverse()
        if self.right:
            elements += self.right.preorder_traverse()
        return elements
        
    def postorder_traverse(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traverse()
            
        if self.right:
            elements += self.right.postorder_traverse()
            
        elements.append(self.data)
        return elements
            
def build_tree(elements):
    root = Node(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])
    return root
    
    
numbers = [2,1,9,4,12,44]
#numbers = [1,2,3,4,5]
res = build_tree(numbers)
print('Inorder Traversal elements are: ',res.inorder_traverse())
print('preorder Traversal elements are: ',res.preorder_traverse())
print('postorder Traversal elements are: ',res.postorder_traverse())
    
    
    
    
    