class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None

    def viewList(self):
        if self.head == None:
            print('List is empty')
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, end=' ')
                temp = temp.next


    #def deleteFirst(self):
     #   if self.head == None:
      #      print('Link list is empty')
       # else:
        #    self.head = self.head.next

    def insertFirst(self,val):
        newNode = Node(val)
        
        if self.head is None:
            print('List is sEmpty')
            
        else:
            newNode.next = self.head
            self.head = newNode


    #to delete at the end
    def deleteLast(self):
        if(self.head == None):
            print('No element in the link list')
        else:
           temp = self.head
           while (temp.next != None):
               prev = temp
               temp = temp.next
           prev.next = None               

    #to insert at the last 
    def insertLast(self, value):
        newNode = Node(value)
        if(self.head==None):
            self.head = newNode
        else:
            temp = self.head 
            while temp.next != None:
                temp = temp.next
            temp.next = newNode


myLinkls = linkedList()
myLinkls.insertLast(1)
myLinkls.insertLast(2)
myLinkls.insertLast(3)
myLinkls.insertLast(4)
myLinkls.insertLast(5)
myLinkls.viewList()
#myLinkls.deleteFirst()
myLinkls.deleteLast()
print()
myLinkls.viewList()
print()
myLinkls.insertFirst(0)
myLinkls.viewList()