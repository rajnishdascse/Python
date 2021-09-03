#spoj accepted ans

from sys import stdin

for i in stdin:
    res = int(i)
    if res ==42:
        break
    print(i)

'''
#my solution

ls=[]
n = int(input())
for i in range(n):
    N = int(input())
    ls.append(N)

for N in ls:
    res = int(N)
    if res== 42:
        break
    print(N)

'''