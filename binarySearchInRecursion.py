key=13
def binarySearch(low,high,key,array):
    if low>high:
        return "Not Found"
    else:

        mid=(low+high)//2
        if array[mid]==key:
           return (f"It is in {mid}th Index")
        elif array[mid]<key:
            low=mid+1
            return binarySearch(low,high,key,array)
        elif array[mid]>key:
            high=mid-1
            return binarySearch(low,high,key,array)
        
array=[0,2,3,4,5,6,7,8,10,13,14]
low=0
high=len(array)-1

print(binarySearch(low,high,key,array))