class bst:
    def __init__(self):
        self.root= None
    
    def insert(self, key):
        '''
        Insert by going deep into tree until you can't anymore.
        Go left if value that you want to insert is less, else go right if it is greater.
        '''
        newNode = node(key)
        if self.root is None:
            self.root = newNode
        else:
            # start at the root.
            currentNode = self.root
            # traverse the tree until you can't anymore. break from the loop once you reach the bottom of the tree.
            while True:
                # if key being inserted is less than the current node, go left. 
                if key < currentNode.key:
                    # if at the bottom of the tree, we can finally insert node.
                    if currentNode.left is None:
                        currentNode.left = newNode
                        newNode.parent = currentNode
                        break
                    currentNode = currentNode.left

                # if key being inserted is greater than current node, go right.
                else:
                    # if at the bottom of the tree, we can finally insert node.
                    if currentNode.right is None:
                        currentNode.right = newNode
                        newNode.parent = currentNode
                        break
                    currentNode = currentNode.right
        return newNode

    def find(self, key):
        '''
        Traverse tree to try and find the element.
        If element is not found because we are at a dead end, return None.
        '''
        # start at the root.
        currentNode = self.root
        # try and find the node by going left or right as appropriate.
        # if no nodes match the value, return None.
        while currentNode is not None:
            if key == currentNode.key:
                return currentNode
            elif key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None

class node:
    def __init__(self, key):
        self.key = key

    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None

def main():
    print("hi, steven!")

if __name__ == "__main__":
    main()