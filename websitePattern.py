username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
combination=[]
from itertools import combinations
#Website in combination
for i in range(len(username)):
    combination.append([username[i],timestamp[i],website[i]])
#Create Value in dictionay
dictValue={}
for i in range(len(combination)):
    dictValue[username[i]]=[]
#appendValue in dictionary
from functools import reduce

for key,values in dictValue.items():
    for i in range(len(username)):
        if key ==combination[i][0]:
            values.append(combination[i][2:])
    values=reduce(lambda x,y:x+y,values)
    dictValue[key]=values
CombinationMostVisited=[]
for key,values in dictValue.items():
    if len(values)<=3:
        CombinationMostVisited.append(values)
    else:
        for i in range(len(values)-2):
            for j in range(i+1,len(values)-1):
                for k in range(j+1,len(values)):
                    CombinationMostVisited.append([values[i],values[j],values[k]])
mostVisited={}
for i in range(len(CombinationMostVisited)):
    tup=tuple((CombinationMostVisited[i]))
    if tup not in mostVisited:
        mostVisited[tup]=1
    else:
        mostVisited[tup]+=1
maxValue=-1
for key,value in mostVisited.items():
    maxValue=max(maxValue,value)
    
    if maxValue ==value:
        print(list(key))
    