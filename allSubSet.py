def helperFunction(index,n,path,answer,nums):
    if index==n:
        answer.append(path[:]) 
        return

    #First Include the Element
    path.append(nums[index])#Left Call Inclusive
    helperFunction(index+1,n,path,answer,nums)

    #This One is Exclusive call or empty subset
    path.pop()
    helperFunction(index+1,n,path,answer,nums)
def usingBacktrackingWithLoop(index,n,path,answer,nums):
    # res will store all subsets.
    # O(2 ^ (number of elements inside array))
    # because at every step we have two choices
    # either include or ignore.
    answer.append(path[:])
    for i in range(index,len(nums)):
        # include the A[i] in subset.
        path.append(nums[i])
        usingBacktrackingWithLoop(i+1,n,path,answer,nums)#i+1 for Index is because it is for avoid duplicate
        #Example:
            #[1,2,2],[1,3,3],[2,2,3],[3,3,3] Like That
        path.pop(-1)
    
    return
def AllSubset(nums):
  n=len(nums)
  index=0
  answer=[]
  path=[]
  usingBacktrackingWithLoop(index,n,path,answer,nums)
  print(answer)
nums=[1,2,3]
AllSubset(nums)

def subsetsUtil(A, subset, index):
    print(*subset)
    for i in range(index, len(A)):
         
        
        subset.append(A[i])
         
        # move onto the next element.
        subsetsUtil(A, subset, i + 1)
         
        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return
 
# below function returns the subsets of vector A.
def subsets(A):
    global res
    subset = []
     
    # keeps track of current element in vector A
    index = 0
    subsetsUtil(A, subset, index)
     
# Driver Code
 
# find the subsets of below vector.
array = [1, 2, 3]
 

subsets(nums)
 