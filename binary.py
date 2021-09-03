n = int(input())
count = 0
highest_numberOfOnes = 0

while n >0:
    if n%2==1:
        count = count+1
        if count > highest_numberOfOnes:
            highest_numberOfOnes = count
    else:
        count = 0
    n = n//2
print(highest_numberOfOnes)


#in this program have to count the conseqative number of 1 