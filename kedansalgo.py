def maxsubarraysum(arr):
    
    res=arr[0]

    #maximum sum of subarray ending at current position
    maxending=0

    start=0
    end=0
    temp_start=0


    for i in range(1,len(arr)):
        
        #if starting new subarray is better

        if arr[i]> maxending + arr[i]:
            maxending=arr[i]
            temp_start=i
        else:
            maxending=maxending+ arr[i]

        #update the global maximum

        if maxending> res:
            res=maxending
            start=temp_start
            end=i
    return res,start,end

arr=[2,3,-8,7,-1,2,3]
max_sum,start,end=maxsubarraysum(arr)
print('Max Sum',max_sum)
print('Starting Index',start)
print('Ending Index',end)