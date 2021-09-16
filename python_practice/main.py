import linkedList
def main():
    # initalize linked list
    list1 = linkedList.linkedList()
    list1.append("mon")

    # add nodes.
    e2 = linkedList.node("tue")
    e3 = linkedList.node("wed")

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
    main()