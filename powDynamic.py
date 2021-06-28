memoization={}
def pow(x,n):
    if n<0:
        print("true")
        x=1/x
        n=-1*n
        return pow(x,n)
    else:
        global memoization
        if n==0:
            return 1
        if n==1:
            return x
        else:
            if n%2==0:
                    memoization[n]= pow(x,n//2)*x
                    return memoization[n]*memoization[n]
            elif n%2==1:
                    memoization[n]= pow(x,n//2)
                    return memoization[n]*memoization[n]
        
x=0.00001
n=2147483647
print(pow(x,n))
print()