
class maxheap:
    '''
    implements max heap: 
    '''
    def __init__(self, maxsize):
        self.size = 0
        self.maxsize = maxsize
        self.Heap = [0] * (self.maxsize + 1)

    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return 2*pos + 1
    
    def isLeaf(self,pos):
        if pos>= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, pos1,pos2):
        self.Heap[pos1], self.Heap[pos2] = (self.Heap[pos2],self.Heap[pos1])
    
    def maxHeapify(self, pos):
        '''
        Function to maxheapify node at position "pos".
        '''
        leftChild = self.Heap[self.leftChild(pos)]
        rightChild = self.Heap[self.rightChild(pos)]

        # if node is a nonleaf and is smaller than its children, it must exchange spots with one of its children.
        if not self.isLeaf(pos):
            if(self.Heap[pos] < leftChild or self.Heap[pos] < rightChild):
                # the node must exchange spots with the biggest child. if left > right, exchange with left. 
                if(leftChild > rightChild):
                   self.swap(pos, self.leftChild(pos))
                   self.maxHeapify(self.leftChild(pos))
                #else , exchange with right.
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))
def main ():
    print("hi")
if __name__ == "__main__":
    main()

