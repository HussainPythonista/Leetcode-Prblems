def findLastIndexOfString(string):
    dictValue={}
    for i in range(len(string)):
        if string[i] in dictValue:
            dictValue[string[i]]=i
        else:
            dictValue[string[i]]=i
    return(dictValue)


def removeDuplicates(string):
    lastIndexs=findLastIndexOfString(string)
    result=[]
    for i in range(len(string)):
        if len(result)==0:
            result.append(string[i])
        else:
            if string[i] not in result:
                if string[i]>string[i]
    
string="cbcacdbc"
removeDuplicates(string)