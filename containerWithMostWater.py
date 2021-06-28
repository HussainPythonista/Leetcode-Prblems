def containerWithMostWater(height):
    """MaxValue=0
    maxCount=0
    
    for i in range(len(height)):
        aPointer=i+1
        minValue=999999999999999999999999999999999
        count=0
        while aPointer<len(height):
            count+=1
            minValue=min(height[i],height[aPointer])
            MaxValue=max(MaxValue, minValue*(aPointer-i))
            aPointer+=1
    print(MaxValue)"""
    maxValue=0
    aPointer=0
    bPointer=len(height)-1
    while aPointer<bPointer:
        minValue=min(height[aPointer],height[bPointer])
        maxValue=max(maxValue,minValue*(bPointer-aPointer))
        if height[aPointer]<height[bPointer]:
            aPointer+=1
        else:
            bPointer-=1
    print(maxValue)
height=[3,9,3,4,7,2,12,6]
#height = [1,8,6,2,5,4,8,3,7]

containerWithMostWater(height)