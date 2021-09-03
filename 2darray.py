arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
maximum = -9*7
for r in range(6):
    for c in range(6):
        if c+2 < 6 and r+2 < 6:
             s = arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
        if s > maximum:
            maximum = s
print(maximum)

"""
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
"""