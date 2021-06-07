def fibonacci(n,mem0):
    if n>1:
        if n not in mem0:
            val=fibonacci(n-1,mem0)+fibonacci(n-2,mem0)
            mem0[n]=val
            return mem0[n]
        else:
            return mem0[n]
    else:
        mem0[n]=n
        return n
n=130
mem0={}
print(fibonacci(n,mem0))
print(mem0)