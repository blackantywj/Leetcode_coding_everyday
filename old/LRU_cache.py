class DLLNode:
    '''
       prev <-|val,key|-> next
    '''
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.next = self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.HeadNode = DLLNode(0,0)
        self.TailNode = DLLNode(0,0)
        '''
           |HeadNode| <-> |TailNode|
        '''
        self.HeadNode.next = self.TailNode
        self.TailNode.prev = self.HeadNode

    def _remove(self,node): # remove from the list
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _insert(self,node): # add at head
        prev_node, next_node = self.HeadNode, self.HeadNode.next
        prev_node.next = node
        node.next = next_node
        node.prev = prev_node
        next_node.prev = node
    
    def get(self, key: int) -> int:
        # return from the cache
        if key in self.cache:
            self._remove(self.cache[key])# remove the node from the list.
            self._insert(self.cache[key])# add it near the head node
            return self.cache[key].val # cache stores Node, so value is extracted.
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key]) # because we want to add it near the head again.
        
        self.cache[key] = DLLNode(key,value)
        
        self._insert(self.cache[key]) # at the head
        
        if len(self.cache) > self.capacity:
            #remove the the node near tail
            lru_node = self.TailNode.prev #lru_node indicates the least recently used node.
            self._remove(lru_node) 
            del self.cache[lru_node.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)