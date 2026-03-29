class Template:
    def binary_search(array,start,end,element):
        while start<=end:
            mid=(start+end)//2
            if array[mid]==element:
                return True
            elif array[mid]<element:
                start+=1
            else:
                end-=1
        if start>=end:
            return False
        return True

bs=Template()
array=list(map(int,input().split(" ")))
print(bs.binary_search(0, len(array)-1, 4))
        