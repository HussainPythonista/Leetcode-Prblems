nums1 = [0,0,0,0,1]
nums2= [1,0,0,0,0]
def commonSubArray(nums1,nums2):#I solve This Problem with Dynamic Programming
    memoization=[[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
    maxValue=0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i]==nums2[j]:
                memoization[i][j]=memoization[i-1][j-1]+1
            else:
                memoization[i][j]=0
            maxValue=max(maxValue,memoization[i][j])
    print(maxValue)


            
        
        
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
        
commonSubArray(nums1,nums2)