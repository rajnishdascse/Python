N = int(input()) # number of command
output =[]
for i in range(0,N):
    inputs = input().split()
    if inputs[0] == 'print':
        print(output)
    elif inputs[0]== 'insert':
        output.insert(int(inputs[1]), int(inputs[2]))
    
    elif inputs[0] == 'remove':
        output.remove(int(inputs[1]))
    elif inputs[0] == 'pop':
        output.pop()
    elif inputs[0]=='append':
        output.append(int(inputs[1]))
    elif inputs[0]=='sort':
        output.sort()
    else:
        output.reverse()

#outputs are like
#5
#insert 0 1
# insert 1 44
#print
# [1,44]
#pop
# print
#[1]
