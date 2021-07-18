def combine(n,k):
        
        def helper(k,nums,index,path,answer):
            #global answer

            if len(path)==k:
                answer.append(path[:])
                return
            for i in range(index,len(nums)):
                print(path)
                path.append(nums[i])
                helper(k,nums,i+1,path,answer)
                path.pop()
            return (answer)
        
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        index=0
        path=[]
        answer=[]
        return (helper(k,nums,index,path,answer))
        
n=4
k=2
print(combine(n,k))