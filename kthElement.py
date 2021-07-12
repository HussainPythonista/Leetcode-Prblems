matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8


def joininingTheList(matrix):
    listVal=[]
    for i in range(len(matrix)):
        listVal+=matrix[i]
    return listVal
def findKthElement(matrix,k):
    listValue=joininingTheList(matrix)
    listValue=list(sorted(listValue))
    print(listValue)
    for i in range(len(listValue)):
        if i==k-1:
            print(listValue[i])
findKthElement(matrix,k)
