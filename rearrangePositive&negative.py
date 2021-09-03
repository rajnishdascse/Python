class Solution:
    def rearrangeArray(self,arr,n):
        i = -1    #pointer
        for j in range(n):
            if arr[j] < 0:
                i+=1    
                arr[i],arr[j] = arr[j],arr[i]     #swap the number, if positive then ignore

            #now all the neg number in the left side and pos nuber on the right side of the array

        pos = i+1     #start from the last point where the i was incremented
        neg = 0

        while (pos <n and neg < pos and arr[neg] <0):
            arr[pos],arr[neg] = arr[neg],arr[pos]
            pos+=1
            neg+=2

    def printArray(self,arr,n):
        for i in range(n):
            print(arr[i],end=' ')

obj = Solution()
arr = [int(i) for i in input().split()]
n = len(arr)
obj.rearrangeArray(arr,n)
obj.printArray(arr,n)
