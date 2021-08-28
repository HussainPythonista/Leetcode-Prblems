string="abcabcbbancd"


#this one is Kadanes and Dynamic Approch and Sliding Window Too
def longestSubSting(string):

        memoization=[]
        i=0
        aPointer=0
        bPointer=1
        memoization=""
        val=1
        maxLength=0
        while bPointer<len(string):
            
            if string[aPointer]!=string[bPointer] and string[bPointer] not in memoization:
                val+=1
                memoization+=string[bPointer]
                bPointer+=1
                
            else:
                memoization=[]
                val=1
                aPointer=aPointer+ 1
                memoization+=string[aPointer]
                bPointer=aPointer+1
            if val>maxLength:
                maxLength=val
        print(maxLength)



#Taken Runtime: 2496 ms
#Memory Usage: 13.9 MB

string="abcabcbbancd"


#Lets Come with efficient one 

def longestSub(s):

    memoiszation={}

    aPointer=0
    bPointer=0
    length=0
    numberOfLetters=len(s)

    while bPointer<numberOfLetters:
        if s[bPointer] in memoiszation:
            aPointer=max(memoiszation[s[bPointer]]+1,aPointer)
        memoiszation[s[bPointer]]=bPointer
        length=max(length,bPointer-aPointer+1)
        bPointer+=1
    return length
s="abcabcbbancd"
print(longestSub(s))
#Runtime=: 52 ms
#Memory Usage=13.6