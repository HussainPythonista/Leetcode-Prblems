count=-1
negative=False
def divideValueWithoutDivison(dividend,divisor):
    negative=False
    sign=1
    if dividend== -2147483648 and divisor == -1:
        return 2147483647
    elif dividend== 2147483648 and divisor == 1:
        return 2147483647
    if divisor<0:
        divisor=-divisor
        sign*=-1
    if dividend<0:
        dividend=-dividend
        sign*=-1

    quotent=0
    while dividend>=divisor:
        count=1
        iDivisor=divisor
        while dividend>=iDivisor+iDivisor:
                iDivisor+=iDivisor
                count+=count
        quotent+=count
        dividend-=iDivisor
    
    if sign<0:
        return -quotent
    else:
        return quotent
        
dividend,divisor=7,-3
print(divideValueWithoutDivison(dividend,divisor))