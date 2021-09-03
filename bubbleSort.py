nums = list(map(int,input().split()))
l = len(nums)
def bubbleSort(nums):
    for i in range(l):
        for j in range(0,l-i-1):     #last element already in place
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
            
            ''' #swapping taking 3rd variable
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                '''

bubbleSort(nums)
print(nums)