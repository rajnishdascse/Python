class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class Solution:
    def insert_data(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                current = self.insert_data(root.left,data)
                root.left = current
            else:
                current = self.insert_data(root.right,data)
                root.right = current
        return root

    def level_order_traversal(self,root):
        queue = []  # take an empty queue
        queue.append(root) #append the root in the queue
        while len(queue) !=0:
            root = queue.pop(0)    #pop the element from the queue and print also append its child node
            print(root.data,end=' ')
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

N = int(input())
obj = Solution()
root = None
for _ in range(N):
    data = int(input())
    root = obj.insert_data(root,data)
obj.level_order_traversal(root)