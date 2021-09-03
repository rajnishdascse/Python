import string
dict={}
data=''
file = open('Ciphermsg.txt','w')
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]   #substitution, can use any number to subtract from i
print(dict)
with open('msg.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print('End of file')
            break
        if c in dict:
            data = dict[c]
        else:
            data =c
            file.write(data)
            print(data)
file.close()
