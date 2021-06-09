nums = [7,8,9,10,11,12,13,1,4,5,6]
nums=[3,1,2]
#nums=[6,7,8,0,1,2,3,4,5,6]

#This one is O(2Logn) Approach is Little slower than O(logn) Approach

search=1
def binarySearch(nums,pivot,start,end,search):
    if pivot==0:
        start=0
        end=len(nums)-1
    elif search>=nums[pivot] and search<=nums[end]:
        start=pivot-1
        end=end
    else:
    
        start=start 
        end=pivot
    
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==search:
            return mid
        else:
            if nums[mid]<search:
                start=mid+1
            else:
                end=mid-1
    else:
        return -1

# Approach 1
#Finding Pivot
pivot=0
def findingPivot(nums,start,end):
    global pivot
    midValue=(start+end)//2
    if nums[midValue]>nums[midValue+1]:
        pivot=midValue+1
        
    else:
        if nums[midValue]>nums[start]:
            start=midValue+1
            end=end
            return findingPivot(nums,start,end)
        else:
            start=start
            end=midValue
            return findingPivot(nums,start,end)
    return pivot
start=0
end=len(nums)-1
if len(nums)>2:
    piviot=findingPivot(nums,start,end)
    result= binarySearch(nums,
    piviot,
    start,
    end,
    search)
    print(result)
else:
    piviot=0
    result= binarySearch(nums,piviot,start,end,search)
    print(result)