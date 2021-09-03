class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def insert_data(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert_data(root.left,data)
                root.left = current
            else:
                current = self.insert_data(root.right,data)
                root.right = current
        return root

    def get_height(self,root):
        if root is None:
            return -1
        return max(self.get_height(root.left), self.get_height(root.right))+1

N = int(input())
root = None
obj = Solution()
for _ in range(N):
    data = int(input())
    root = obj.insert_data(root,data)
height = obj.get_height(root)
print('The height of the Tree is: ',height)

