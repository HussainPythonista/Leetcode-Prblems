

def medianInArray(nums1, nums2):
    continuousValue = [0 for _ in range(len(nums1)+len(nums2))]
    i = 0
    while i <= len(nums1)-1:
        continuousValue[i] = nums1[i]
        i += 1

    aPointer = len(nums1)-1
    bPointer = len(continuousValue)-1
    numsPointer = len(nums2)-1
    while aPointer >= 0 and numsPointer >= 0:
        if continuousValue[aPointer] > nums2[numsPointer] :
            continuousValue[bPointer] = nums1[aPointer]
            aPointer -= 1
            
        else:
            continuousValue[bPointer] = num2[numsPointer]
            numsPointer -= 1
        
        bPointer -= 1
    while numsPointer >= 0:
        continuousValue[bPointer] = nums2[numsPointer]
        numsPointer -= 1
        
        bPointer -= 1
    return callMedian(continuousValue)

def callMedian(array):
    print(array)
    aPointer=0
    bPointer=len(array)-1
    
    mid=aPointer+bPointer/2
    if mid%1==0:
       mid=int(mid)
       return array[mid]
    else:
        mid=int(mid)

        median=array[mid]+array[mid+1]
        return median/2

    
num1 = [1,2]
num2 = [3,4]
print(medianInArray(num1, num2))
