def rotate(arr,N):
    x = arr[N-1]
    for i in range(N-1,0,-1):
        arr[i] = arr[i-1]
    arr[0]=x

N = int(input())
arr = [int(i) for i in input().split()]
for i in range(N):
    print(arr[i],end=' ')
print()
rotate(arr,N)
for i in range(N):
    print(arr[i],end=' ')



# def rotate(arr,N):
#     x = arr[N-1]
#     for i in range(N-1,0,-1):
#         arr[i]= arr[i-1]
#     arr[0]=x


# arr = [1,2,3,4,5]
# N = len(arr)
# rotate(arr,N)
# for i in range(N):
#     print(arr[i],end=' ')

