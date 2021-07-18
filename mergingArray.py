from typing import NoReturn


nums1=[4,5,6,7,10,20]
num2=[8,9,11,12,15]
num3=[0 for i in range(len(nums1)+len(num2))]
print(num3)
k=0
aPointer=0
bPointer=0
while aPointer<=len(nums1)-1 and bPointer<=len(num2)-1:
    if nums1[aPointer]<num2[bPointer]:
        num3[k]=nums1[aPointer]
        aPointer+=1
        k+=1
    else:
        num3[k]=num2[bPointer]
        bPointer+=1
        k+=1
while bPointer<=len(num2)-1:
    num3[k]=num2[bPointer]
    bPointer+=1
    k+=1
while aPointer<=len(nums1)-1:
    num3[k]=nums1[aPointer]
    aPointer+=1
    k+=1
print(num3)