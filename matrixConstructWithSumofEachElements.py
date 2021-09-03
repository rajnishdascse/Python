r = int(input('Enter number of rows: '))
c = int(input('Enter number of cols: '))

matrix=[]
for i in range(r):
    ls = []
    for j in range(c):
        ls.append(int(input('Enter element ')))
    matrix.append(ls)

#----print---

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=' ')
    print()
    
#to calculate sum of each element in the matrix

sum =0
for i in range(r):
    for j in range(c):
        sum += matrix[i][j]
print('The sum of the elements are: ', sum)