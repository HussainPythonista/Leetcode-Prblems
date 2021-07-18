def divideTwoInteger(divide,divisor):
    while divide>divisor:
        count=1
        fastDivisor=divisor
        while divide>=fastDivisor+fastDivisor:
            fastDivisor=fastDivisor+fastDivisor
            count+=count
        divide-=fastDivisor
        return count
divide=100
divisor=3
print(divideTwoInteger(divide,divisor))