print("Hello world")

#Implement DoublyLinkedList

class Node(object):
    def __init__(self,key,val,nextRef=None,prevRef=None):
        self.val=val
        self.key=key
        self.nextRef=nextRef
        self.prevRef=prevRef

class DoublyLinkedList(object):
    def __init__(self):
        self.head=None
        self.last=None
    def inserValueBegin(self,key,val):
        if self.head==None:
            node=Node(key,val)
            self.head=node
            self.last=self.head
        
        else:
            node=Node(key,val)
            node.nextRef=self.head
            self.head.prevRef=node
            self.head=node
            #self.last.prevRef=self.head
        return self.head
    
    def deleteNode(self,node):
        if self.head.nextRef!=None:
            next=node.nextRef
            prev=node.prevRef
            
            if node==self.last :
                tempPrev=node.prevRef
                self.last=tempPrev
                node.prevRef.nextRef=None
    
            else:
                node.nextRef.prevRef=prev
                node.prevRef.nextRef=next
        
            
            
    def printVal(self):
        if self.head==None:
            print(None)
        else:
            pointer=self.head
            forward=""
            while pointer:
                forward+=str(pointer.val)+"-->"
                pointer=pointer.nextRef
            print(forward)

    def lastElement(self):
        pointer=self.head
        while pointer.nextRef:
            #print(pointer.data)
            pointer=pointer.nextRef
        return (pointer)
    def printBackWord(self):
        pointer=self.lastElement()
        backword=""
        while pointer:
            backword+=str(pointer.val)+"<--"
            pointer=pointer.prevRef
        print(backword)
    

capacity=1
bucket={}
dd=DoublyLinkedList()
#[null,null,1,null,-1,2]
def get(key):
    result=-1
    if dd.head.key==key:
        result=dd.head.val
    else:
    #result=-1
        if key in bucket:
            node=bucket[key]
            dd.deleteNode(node)
            address=dd.inserValueBegin(key,node.val)
            bucket[key]=address
            result=node.val
    return result 
def LRUCache(capacity,val):
    global bucket,dd
    key=val[0]
    value=val[1]
    if key in bucket:
        address=bucket[key]
        dd.deleteNode(address)
        address=dd.inserValueBegin(key,value)
        bucket[key]=address
    elif len(bucket)==capacity:
            lastNode=dd.last
            print([lastNode.val])
            #bucket.pop(lastNode.key)
            dd.deleteNode(lastNode)
            
            newAdress= dd.inserValueBegin(key,value)
            bucket[key]=newAdress
    else:
        address=dd.inserValueBegin(key,value)
        bucket[key]=address
    
    #dd.printVal()
    #else:
    #dd.printVal()
#[[2], , [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
#[null,null,1,null,-1,2]
val=[2, 1]
LRUCache(capacity,val)
get(2)
val=[3, 2]
LRUCache(capacity,val)
print(get(2))
print(get(3))
dd.printVal()
dd.printBackWord()
print(bucket)