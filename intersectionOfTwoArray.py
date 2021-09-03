def intersection(arr1,arr2,a,b):
    i,j =0,0
    while i < a and j < b:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            print(arr2[j],end=' ')
            i+=1
            j+=1




arr1 = [1,2,5,4,9,10,11]
arr2=[1,5,8,12]
a = len(arr1)
b = len(arr2)
intersection(arr1,arr2,a,b)