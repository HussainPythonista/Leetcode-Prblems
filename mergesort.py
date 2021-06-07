
def valuesToSort(nums1, m, nums2, n):
    aPointer=m-1
    bPointer=len(nums1)-1
    numsPointer=n-1
    while aPointer>=0 and numsPointer>=0:
    #first Change Those Things As MY convienience
        if nums2[numsPointer]>nums1[aPointer]:
            nums1[bPointer]=nums2[numsPointer]
            numsPointer-=1
            bPointer-=1
        elif nums2[numsPointer]<=nums1[aPointer]:
            nums1[bPointer]=nums1[aPointer]
            aPointer-=1
            bPointer-=1

    print(nums1)
    while numsPointer>=0:
        nums1[bPointer]=nums2[numsPointer]
        numsPointer-=1
        bPointer-=1
    
nums1 = [1,3,0,0,0]
m = 2
nums2 = [2,5,6]
n = 3
print(valuesToSort(nums1, m, nums2, n))
