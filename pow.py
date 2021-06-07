powValue=0
def pow(x,n):
    if n>0:
        if n%2==0:
            return pow(x,n//2)*pow(x,n//2)
        elif n%2==1:
            return pow(x,n//2)*pow(x,n//2)*x
    if n==0:
        return 1
number=5
n=5
print(pow(number,n))



