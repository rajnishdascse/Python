class Pal:
    def __init__(self):
        self.stack = list()
        self.queue = list()
        return None

    def push_into_stack(self,char):
        self.stack.append(char)
    def pop_from_stack(self):
        return(self.stack.pop(-1))
    def enque_char(self,char):
        self.queue.append(char)
    def deque_char(self):
        return(self.queue.pop(0))


n = input()
s = Pal()
l = len(n)
for i in range(l):
    s.push_into_stack(n[i])
    s.enque_char(n[i])
isPalindrom = True

for i in range(l//2):
    if s.pop_from_stack() != s.deque_char():
        isPalindrom = False
        break
if isPalindrom:
    print('string '+ n + ' is Palindrom')
else:
    print('string ' + n + ' is not Palindrom')
