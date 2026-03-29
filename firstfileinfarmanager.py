def binarySearch(arr,start,end,element):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==element:
            return True
        elif arr[mid]>element:
            end-=1
        else:
            start+=1
    if start>end:
        return False
    return True

arr=[1,23,45,7]
print(binarySearch(arr,0,len(arr)-1,8))
