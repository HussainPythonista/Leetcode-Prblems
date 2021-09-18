string="cbcacdbc"

def removeLettersFromString(string):
    dictVal={}
    dummyList=[None for i in range(len(string))]
    for i in range(len(string)):
        if string[i] not in dictVal:
            dummyList[i]=string[i]
            dictVal[string[i]]=i
        else:
            dummyList[dictVal[string[i]]]=None
            dictVal[string[i]]=i
            dummyList[dictVal[string[i]]]=string[i]
    print(dictVal,dummyList)
removeLettersFromString(string)