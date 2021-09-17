


def insertion_sort(list_unsorted):
    '''
    For i = 1,2,... n
    insert A[i] into sorted array A[0:i-1]
    note that binary insertion sort could help if O(comparions) > O(swaps)
    '''
    print("running insertion sort...")
    
    # swap first two elements (i=1 case).
    if(list_unsorted[1] < list_unsorted[0]):
                list_unsorted[1], list_unsorted[0] = list_unsorted[0] , list_unsorted[1]

    # step thru remainder of list.
    for i in range(2, len(list_unsorted) ):
        # swaps to sort list.  
        for j in range(i-1 , -1, -1):
            if list_unsorted[i] < list_unsorted[j]:
                list_unsorted[i], list_unsorted[j] = list_unsorted[j] , list_unsorted[i]
                i = i -1
            else:
                break

    

    return list_unsorted

def main():
    ''' 
    Here I'll study different sorting algos. 
    Types:
        -Insertion Sort
        -Bubble Sort.
        -Merge Sort
        -Quick Sort.
        -Heap Sort
        -Selection Sort.

        -Comparison Sort (ran by python)
        -For specific situations:
            -cock tail sort, etc. may be more efficient for certain applications 
    Motivation:
        -Finding median.
            -Takes O(1) time with a sorted list.
        -Binary Search O(log n )
            -Otherwise, if random, linear search takes linear time. 
        -Data Compression
            -Sorting items finds duplicates, if i have identical items, can just store item and num items.
        -Computer Graphics.
            -Rendering in order is more efficient for opacity.
        
    '''
    list1 = [5,2,4,6,1,3,10,52364, 12,2,34,1235,2]
    list2 = insertion_sort(list1)
    print("sorted list: " , list2)
if __name__ == "__main__":
    main()
