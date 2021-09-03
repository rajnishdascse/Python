#linked list implementation in queue
# to implement queue and stack operation we use deque from collection module

# since we know that stack follow LIFO and Queue follows FIFO operation

from collections import deque
linked_list = deque()
linked_list.append(0)

linked_list.appendleft(1)   #it will append from beginning of the list  [1,0]
#linked_list.pop()  #will pop 1 from the list
linked_list.append(2)    #[1,0,2]
linked_list.pop()    # will pop 2
#linked_list.popleft()   #will pop 1
print(linked_list)

print('----xxxx-----')

#Queue
queue = deque()
#adding element to the queue
for i in range(0,5):
    queue.append(i)
    print(queue)

print('---Queue poping from here---')
#implemting queue to remove element
for i in range(len(queue)):
    queue.popleft()
    print(queue)

 #Stack LIFO implementation
 
print('---Stack LIFO---')
stack = deque()
for i in range(0,5):
    stack.appendleft(i)
    print(stack)
    
#pop
print('---Poping from stack---')
for i in range(len(stack)):
    stack.popleft()
    print(stack)