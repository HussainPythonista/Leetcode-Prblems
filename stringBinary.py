def binaryValues(n):
    bin1="1"
    a=["0","1"]
    i=2
    for _ in range(2,n,2):
        for j in range(2):
            new=bin1+str(j)
            a.append(new)
            #if len(a)==n:
            #    break
        bin1=a[i]
        i+=1
       
    print(a) 
binaryValues(100)