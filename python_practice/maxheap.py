
class maxheap:
    '''
    implements max heap: 
    '''
    def __init__(self):
        self.size = 0

    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return 2*pos + 1
        

def main ():
    print("hi")
if __name__ == "__main__":
    main()

