def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1

        while (j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
        

arr = [6,5,2,3,1,4]
print(InsertionSort(arr))