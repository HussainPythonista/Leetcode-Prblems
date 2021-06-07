""""def binaryAdd(a,b):
    carry=0
    result=""
    a,b=list(a),list(b)
    while a or b or carry==1:
        if a:
            carry+=int(a.pop())
        if b:
            carry+=int(b.pop())
        result+=str(carry%2)
        carry=carry//2
    return result


a="11"
b="1"
print(binaryAdd(a,b))"""

def MyApproach(a,b):
    carry=0 #This One Hold th value in top of addtion
    ListA=list(a)
    ListB=list(b)
    result=""
    while ListA or ListB or carry==1:
        if ListA:
            carry+=int(ListA.pop())
        if ListB:    
            carry+=int(ListB.pop())
            
        result+=str(carry%2)
        carry=carry//2
    print(result[::-1])
       
a="11"
b="1"
MyApproach(a,b)