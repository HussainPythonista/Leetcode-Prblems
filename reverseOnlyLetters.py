s = "7_28]"
#s="a-b-c"
s=(list(s))

def swap(string,aPointer,bPointer):
    return string[bPointer:] + string[:aPointer]
def reverseOnlyLetters(s):
    aPointer=0
    bPointer=len(s)-1
    #smallLetters=[chr(i) for i in range(97,97+26)]
    #capitalLetters=[chr(i) for i in range(65,65+26)]
    #print(chr(65))
    while aPointer<bPointer:

        if s[aPointer].isalpha() and s[bPointer].isalpha():
            #if (ord(s[bPointer]))!=45:
            s[aPointer],s[bPointer]=s[bPointer],s[aPointer]
            aPointer+=1
            bPointer-=1
        elif s[aPointer].isalpha()==True and s[bPointer].isalpha()==False:
            bPointer-=1
        elif s[aPointer].isalpha()==False and s[bPointer].isalpha()==True:

                aPointer+=1
        else:
            aPointer+=1
            bPointer-=1
        #print(chr(64))
    #"j-Ih-gfE-dCba"
    #for i in range(33,123):
    #"Qedo1ct-eeLg=ntse-T!"
#    [33, 122]
    joined="".join(s)
    return(joined)
print(reverseOnlyLetters(s))