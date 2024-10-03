def bubbblesort(arr):
    n=len(arr)
    for i in range(len(arr)):
        swapped=False
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break;
    return arr
arr=[23,15,77,98,1,4,12]
print(bubbblesort(arr))
