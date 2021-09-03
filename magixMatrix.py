def magicSquareGenerate(n):
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for i in range(n)] for j in range(n)]

    #intilialize position of 1
    i = n/2
    j = n-1

    # Fill the magic square
    # by placing values
    num = 1

    while(num <= (n*n)):
        if i ==-1 and j ==n:
            i = 0           #condition 3
            j = n-2
        else:
            if i < 0:
                i = n-1
            if j == n:
                j = 0
        if magicSquare[int(i)][int(j)]:      #condition 2
            i = i +1
            j = j -2
            continue
        else:
            magicSquare[int(i)][int(j)]=num
            num +=1
        
        i = i -1          #condition 1 
        j = j+1
            
    print('Magic Square of n is ', n)
    print('Sum of each row or column ', n*(n*n+1)/2, '\n')

    for i in range(n):
        for j in range(n):
            print('%2d' %magicSquare[i][j],end=' ')

            #to display output in matrix form
            if j == n-1:
                print()
       # print()
    

n = int(input('Enter a number to get the magic square (only odd number): '))
magicSquareGenerate(n)

