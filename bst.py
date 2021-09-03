class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data: #check is the data already present , if yes then return
            return
        if data < self.data:   #if data is less than the root node then go to left subtree
            if self.left:     #again check is there any data on the left side 
                self.left.add_child(data)    #if data is there than call the add child function
            else:
                self.left = BinarySearchTreeNode(data)  # if there is no data then add data 
        else:
            if self.right:            #same for the right node like we did in left node
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
#inorder traversal, the main motive by doing this to print the elements
    def inorderTraversal(self):
        elements =[]

        #visit left tree
        if self.left:
            elements += self.left.inorderTraversal()    
        
        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.inorderTraversal()
        return elements

#search element in the binary tree
    def search(self,value):
        if value == self.data:   # if data is equal with search data then congrats we got the element at the first place
            return True
        else:
            if value < self.data:
                if self.left:
                    return self.left.search(value)
                else:
                    return False
            if value > self.data:
                if self.right:
                    return self.right.search(value)
                else:
                    return False
    
def build_tree_element(elements):
    root = BinarySearchTreeNode(elements[0])    #assign first element as a root element
    
    for i in range(len(elements)):
        root.add_child(elements[i])     
    return root

numbers = [17,4,1,20,9,23,18,34,4]
numbers_tree = build_tree_element(numbers)
print(numbers_tree.inorderTraversal())
print(numbers_tree.search(4))