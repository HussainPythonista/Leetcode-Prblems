sumValue=0
def sumOfNaturalNumbers(n):
    if n==0:
        return 0
    else:
       
       n+= sumOfNaturalNumbers(n-1)
    return n
    
        
def factorial(n):
    if n==0 or n==1:
        return 1
    
    else:
        return factorial(n-1)*n
    
def PowusingRecursion(n,power):
    if power==0:
        return 1
    if power>0:
        if power>1:
            
            if power%2==0:
                return PowusingRecursion(n,power//2)*PowusingRecursion(n,power//2)
            else:
                return PowusingRecursion(n,power//2)*PowusingRecursion(n,power//2)
        return n
    else:
        n=1/n
        power=-power
        return PowusingRecursion(n,power)
power=0
number=2
print(PowusingRecursion(number,power))


