"""
#printing pattern
# # # #
# # # #
# # # #
# # # #
"""
"""
n = int(input())
for i in range(n):
    for j in range(n):
        print('#', end="")
    print()
"""
"""
#pattern 2
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(" * ", end="")
    print()

"""
#pattern 3
n = int(input())
for i in range(n):
    for j in range(n-i):
        print(' * ', end = '')
    print()

