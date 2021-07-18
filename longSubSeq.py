
def subSequence(nums,prev,current):
    if len(nums)==current:
        return 0
    include=0
    
    if nums[current]>prev:
        
        include=1+subSequence(nums,nums[current],current+1)
        
    exclude=subSequence(nums,prev,current+1)
    maxSeq=max(include,exclude)
    
    return maxSeq
   

nums=[4,10,4,3,8,9]
prev=0
current=0
print(subSequence(nums,prev,current))
