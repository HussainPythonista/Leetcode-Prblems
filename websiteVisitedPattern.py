from collections import defaultdict
from itertools import combinations
from sys import api_version
from typing import final
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
userDetails=[]
analyse=defaultdict(list)

for i in range(len(timestamp)):
    userDetails.append([username[i],timestamp[i],website[i]])
for name,timeStamp,website in userDetails:
    analyse[name].append(website)
    
combinationsValue=[]
resultant=[]
for keys,values in analyse.items():
    
    if len(values)>3:
        for i in range(len(values)-2):
            for j in range(i+1,len(values)-1):
                for k in range(j+1,len(values)):#This Code Also gives Same 3 Value Pairs
                    combinationsValue.append((values[i],values[j],values[k]))
                    resultant.append((values[i],values[j],values[k]))

        analyse[keys]=combinationsValue
    else:
        values=tuple(values)
        resultant.append(values)
        #analyse[keys]=list(combinations(values,3))
finalDictionary={}

for i in range(len(resultant)):
    if resultant[i] not in finalDictionary:
        finalDictionary[resultant[i]]=1
    else:
        finalDictionary[resultant[i]]+=1
sortedValue=sorted(finalDictionary.values(),reverse=True)
for key,val in finalDictionary.items():
    if sortedValue[0]==val:
        print(list(key))