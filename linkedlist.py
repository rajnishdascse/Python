class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None    
    
    def insertAtFirst(self,data):
        node=Node(data,self.head)
        self.head = node   #without this the linked list will be empty

    #insert at end
    def insertEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        #if list is not empty we have to iterate through the list to reach the last element
        itr = self.head
        while itr.next:
            itr = itr.next
       #and when we reach at the end add the data
        itr.next = Node(data,None)    
    
  # to get the length of the list
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
 
    #remove at given index
    def remove_at_index(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        
        count =0
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count +=1

#insert at given index
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index, enter a correct number!!')

        if index ==0:
            self.insertAtFirst(data)
            return
        count =0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

#print the the linked list
    def print(self):
        if self.head is None:
            print('LinkedList is empty')
        
        itr = self.head        #to iterate through the linked list
        LinkedListstr = ''
        while itr !=None:
            LinkedListstr += str(itr.data)+'-->'       #append values
            itr = itr.next
        print(LinkedListstr)
        

obj = LinkedList()
obj.insertAtFirst(1)
obj.insertAtFirst(2)
obj.print()
obj.insertEnd(3)
obj.print()
obj.insert_at(0, 9)  #(index, data)
obj.print()
print('Total number of element in the Linked list is :',obj.get_length())
obj.remove_at_index(2)
obj.print()