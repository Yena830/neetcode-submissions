class Node:
    def __init__(self,key,val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.cachemap = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    def addFirst(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    
    def remove(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre


    def get(self, key: int) -> int:
        if key not in self.cachemap:
            return -1
        node = self.cachemap[key]
        self.remove(node)
        self.addFirst(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            node = self.cachemap[key]
            self.remove(node)
        node = Node(key,value)
        self.addFirst(node)
        self.cachemap[key] = node
        if len(self.cachemap)>self.capacity:
            last = self.tail.prev
            self.remove(last)
            del self.cachemap[last.key]
        
