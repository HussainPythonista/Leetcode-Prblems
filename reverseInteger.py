# On may31-2021
listValue=[-1,-2]

x=-2147483648
def youtubeApproach(x):
    reversedValue=0
    negative=False
    if x<0:
        negative=True
        x=-x
    while x!=0:
        reversedValue*=10
        
        reversedValue+= (x%10)
        x=x//10
    if negative==True:
        reversedValue=-reversedValue
    if abs(reversedValue)<2**31 and reversedValue != 2**31 - 1:
        

        print(reversedValue)
    else:
        print(0) 
def MyApproach(x):
    negative=False
    if x<0:
        negative=True
    
    strOfStr=str(x)
    if strOfStr[0]=="-":
        reversedInteger=strOfStr[:0:-1]
    else:
        reversedInteger=strOfStr[::-1]
    reversedValue=int(reversedInteger)
    if negative==True:

        reversedValue=-reversedValue
    if abs(reversedValue)<2**31 and reversedValue != 2**31 - 1:

            return  reversedValue
    else:
            return 0

     
print(MyApproach(x))
  
