def PrintUnion(arr1,arr2,a,b):
    i,j=0,0
    while i < a and j < b:
        if arr1[i] < arr2[j]:
            print(arr1[i],end=' ')
            i+=1
        elif arr1[i] > arr2[j]:
            print(arr2[j],end=' ')
            j+=1
        else:
            print(arr2[j],end=' ')
            i+=1
            j+=1
    while(i <a):
        print(arr1[i],end=' ')
        i+=1
    while j<b:
        print(arr2[j],end=' ')
        j+=1


arr1 = [1,2,5,6,9]
arr2=[3,4,5,9,10]
a = len(arr1)
b = len(arr2)
PrintUnion(arr1,arr2,a,b)
