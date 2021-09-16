
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    '''
    This linked list class implements a linked list in python. 
    '''
    def __init__(self):
        ''' 
        Constructor 
        '''
        self.head = node()
    

    def append(self, data):
        '''
        append() adds a node to the end of the linked list:
            -if head has no data, append data to it.
            -start from head, and go until next is not defined. Append data there.
        '''
        if self.head.data is None:
            self.head = node(data)

        current = self.head
        while(current.next is not None):
            current = current.next

        current.next = node(data)

    def prepend(self, data):
        '''
        prepend() adds a node to the beginning of the linkedlist and makes it head value:
            -initialize newhead as a node.
            -newhead.next should point to old head.
            -now set self.head to the newhead.
            -this fx assumes self.head exists from __init__() 
        '''
        newhead = node(data)
        newhead.next = self.head
        self.head = newhead

    def deleteWithValue(self, data):
        '''
        deleteWithValue() deletes node with node.data == data from linkedList by erasing all nodes pointing to it.
            -if node we want to delete is head node, just make self.head = self.head.next.
            -else 
                -walk thru linkedlist and stop one before the element we want to delete.
                -once stopped, just point the current.next to the node one AFTER the next node. (current.next.next)
        '''
        if(self.head.data is None):
            return

        if(self.head.data ==data):
            self.head = self.head.next

        current = self.head
        while(current.next is not None):
            if(current.next.data == data):
                current.next = current.next.next
                return
            current = current.next

def main():
    # initalize linked list
    list1 = linkedList()
    list1.append("mon")

    # add nodes.
    e2 = node("tue")
    e3 = node("wed")

    #set next values.
    list1.head.next = e2
    e2.next = e3
   
    #append to linkedlist.
    list1.append("thurs")

    print(list1.head.data)
    print(list1.head.next.data)
    print(list1.head.next.next.data)
    print(list1.head.next.next.next.data)

    print(" ")

    #try prepending:
    list1.prepend("sun")
    print(list1.head.data)
    print(list1.head.next.data)
    print(list1.head.next.next.data)
    print(list1.head.next.next.next.data)

    print(" ")
    
    #Try deleting Mondays:
    list1.deleteWithValue("mon")
    print(list1.head.data)
    print(list1.head.next.data)
    print(list1.head.next.next.data)
    print(list1.head.next.next.next.data)
    
if __name__ == "__main__":
    print("linkedList.py is being run directly")
    main()
else:
    print("linkedList.py is being imported into another module")