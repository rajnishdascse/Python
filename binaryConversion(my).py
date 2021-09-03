def binary_convert(n):
    if n >= 1:
        binary_convert(n//2)
        print(n%2, end=" ")
        
num = int(input())
binary_convert(num)

"""
#using bin built in function

from binary import binary_convert

n = int(input())
binary_convert = bin(n)
print(binary_convert)

"""