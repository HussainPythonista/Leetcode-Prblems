get(2)
val=[3, 2]
LRUCache(capacity,val)
get(2)
get(3)
dd.printVal()
"""
val=[2, 2]

LRUCache(capacity,val)
g=1
get(g)

val=[3, 3]
LRUCache(capacity,val)
print(bucket)
g=2
print(get(g))
dd.printVal()

val=[3, 3]
LRUCache(capacity,val)
val=[4, 4]
LRUCache(capacity,val)
ef isolate():
    node=self.bucket[key]
        if node!=None:
            node.value=val
            self.remove(node)
            self.add(node)
        else:
            if len(self.bucket)==self.capacity:
                self.bucket.pop(self.tail.prev.key)
                self.remove(self.tail.prev)
            newNode=Node(key,value)
            self.bucket[key]=node
            self.add(newNode)
                
        
    def add(self,valueIWantAdd):
        node=valueIWantAdd
        
        headNext=node.next
        self.head.next=node
        node.prev=self.head
        node.next=headNext
        headNext.prev=node
    def remove(self,valueIwantDelete):
        deleteNode=valueIwantDelete#For some understanding purpose
        
        nextRef=deleteNode.next
        prevRef=deleteNode.prev
        
        deleteNode.prev.next=nextRef
        deleteNode.next.prev=prevRef"""