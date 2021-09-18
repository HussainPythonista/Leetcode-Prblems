nums=[1,2,3,4]
val = nums
answerIwant = []
bucket=[]
def permutation(nums):
    global answerIwant,bucket
    if len(nums)==0:
        answerIwant.append(bucket[:])
        
    for i in range(len(nums)):
        val=nums.pop(0)
        bucket.append(val)
        permutation(nums)
        #sub.append(bucket)
        nums.append(bucket.pop())
    return answerIwant
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
sub = []
bucket = []
print(sorted(answerIwant))
val = (permutation(nums))
print(val)

