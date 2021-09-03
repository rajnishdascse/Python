def shell_sort(arr):
    n = len(arr)
    gap = n//2
                                    #['21',38,29,'17',4,25,'11',32,9]   'element'--gap values position
   
    while gap>0 :
       
        for i in range(gap,n):
            key = arr[i]
            j = i  #this one for subtracting purpose   21  17  11, in this key is 17 and j is just holding the key.
            
            while j >= gap and key < arr[j-gap]:  # j-gap means we are comparing 17 with its left element, since we have hold the key in j so we will go back thorgh j-gap (gap is the distance we have caluculated)
                arr[j] = arr[j-gap]
                j = j - gap    # suppose while we are at gap value of the array we are comparing it by reducing the gap
            arr[j] = key
            #through the for loop key is shifting into next element
        gap = gap//2      #reducing the gap
        
arr= [21,38,29,17,4,25,11,32,9]
#arr = [4,31,11,17,21,25,29,38,9]
shell_sort(arr)
print(arr)