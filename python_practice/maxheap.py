
class maxheap:
    '''
    implements max heap: 
    '''
    def __init__(self, maxsize):
        '''
            initialize an empty max heap with a max size.
        '''
        self.size = 0
        self.maxsize = maxsize
        self.Heap = [0] * (self.maxsize + 1)
        self.root = 1
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

    def buildMaxHeap(self, array):
        '''
        -Initialize with unsorted array.
        -Overwrite current data with array being inputted. 
        '''
        # clear out nodes and reinitialize variables
        self.size = len(array)
        self.Heap = [0] * (self.maxsize + 1)

        # set elements inside of heap, unsorted.
        for i in range(1, self.size + 1):
            self.Heap[i] = array[i]

        # create a max heap.
        for i in range(self.size//2, 0, -1):
            self.maxHeapify(i)

    def Print(self):
        '''
            Function to print the contents of the heap
        '''
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
def main ():
    maxheap1= maxheap(100)
    list1 = [6,1,5,3,7,4,9,8,10]
    maxheap1.buildMaxHeap(list1)
    maxheap1.Print()
if __name__ == "__main__":
    main()

