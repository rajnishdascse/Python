def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_array(left,right,arr)

def merge_two_sorted_array(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:      #in this case a[i] is left array[i] and b[j] is the right[j]
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    #for the remaining elements, if the size of both divided array is not equal
    while i < len(a):
        arr[k] = a[i]
        i+=1
        k+=1

    while j <len(b):
        arr[k] = b[j]
        j+=1
        k+=1

arr= [10,3,15,7,18,98,29,-1]
merge_sort(arr)
print(arr)
