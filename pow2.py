def myPow(x,n):
        if abs(n)>1:
            if n%2==0:
                return myPow(x,abs(n)//2)*myPow(x,abs(n)//2)
            elif n%2==1:
                return myPow(x,abs(n)//2)*myPow(x,abs(n)//2)*x
        else:
            return 1/x
x=2
n=-2
print(print(myPow(x,n)))
print(abs(0.44528))
print(int(0.44))
2147483647