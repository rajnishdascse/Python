row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of cols: '))
matrix=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input(str(i) +" "+ str(j)+" : ")))
    matrix.append(a)

#for printing the 2d array
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
