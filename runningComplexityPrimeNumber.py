def isPrime(num):
    for i in range(2,int(num**0.5)+1):    #necessary for time complexity
        if num%i==0:
            return False
    else:
        return True



N = int(input())
for i in range(N):
    number = int(input())
    if isPrime(number):
        print('Prime')
    else:
        print('Not prime')
