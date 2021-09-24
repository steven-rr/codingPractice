
import math
import maxheap 
def merge(list, begin, mid, end):
    '''
        Does merging by finger point algorithm.
    '''        
    sizeL = mid - begin + 1
    sizeR = end- mid

    # create temp arrays:
    arrL = [0] * (sizeL)
    arrR = [0] * (sizeR)

    # copy from begin to mid.
    for i in range( 0, len(arrL) ):
        arrL[i] = list[begin + i]
    # copy from mid+1 to end.
    for i in range( 0 , len(arrR) ): 
        arrR[i] = list[mid + 1 + i]
    
    idxL = 0
    idxR = 0
    idx =begin
    # finger pointing comparison algo.
    while idxL < sizeL and idxR < sizeR:
        if arrL[idxL] <= arrR[idxR]:
            list[idx] = arrL[idxL]
            idxL = idxL + 1
        else:
            list[idx] = arrR[idxR]
            idxR = idxR + 1
        idx = idx +1

    # if sizeL not equal sizeR, we must copy remaining elements of bigger sublist into list.
    while idxL <  sizeL:
        list[idx] = arrL[idxL]
        idxL = idxL + 1
        idx = idx + 1

    while idxR < sizeR:
        list[idx] = arrR[idxR]
        idxR = idxR + 1
        idx = idx + 1

def merge_sort(list_unsorted, begin, end):
    '''
        Standard recusion algorithm.
        Complexity: O( n log ( n ) )
        Split Array A into two parts:
                L     R
                (sort) (sort)
                L'    R'
                    (MERGE)
            This yields sorted Array
        
        -The merge function assumes you have two sorted arrays.
        -The merge function uses a two finger algo.
            -Keep splitting until you can't anymore, then merge leaves. Then merge two pairs.
            -Example:
                [2, 7, 13, 20] and [1, 9, 10, 11]   
                [1, 2, 7, 9, 11, 12, 13, 20]
        -Complexity Proof:
            T is work done. 

            T(n) = c1 + 2 * T( n/2 ) + c2 * n, where c1 and c2 are constants

                    cn                | 
            cn/2           cn/2        |   --> (1 + log n layers), each layer you do cn work to sort.
        cn/4 cn/4       cn/4 cn/4     |
                    ....               |
        c c c c c c c c c c c c c c c c  --> (n leaves)

        => T(n) = ( 1 + log(n) ) * cn = O( n log(n) )
        
        -Disadavantage: SPACE COMPLEXITY. O(n) space complexity. Insertion sort space complexity is O(1).
    '''
    # return recursively.
    if (begin >= end):
        return
    # here, there's a 
    mid = begin + math.floor( (end - begin) /2 )
    merge_sort(list_unsorted, begin, mid)
    merge_sort(list_unsorted, mid+1, end)
    merge(list_unsorted, begin, mid, end)

def insertion_sort(list_unsorted):
    '''
        For i = 1,2,... n
        insert A[i] into sorted array A[0:i-1]
        note that binary insertion sort could help if O(comparions) > O(swaps)
    '''
    print("running insertion sort...")
    
    list_sorted = list_unsorted[:]
    # swap first two elements (i=1 case).
    if(list_sorted[1] < list_sorted[0]):
                list_sorted[1], list_sorted[0] = list_sorted[0] , list_sorted[1]

    # step thru remainder of list.
    for i in range(2, len(list_sorted) ):
        # swaps to sort list.  
        for j in range(i-1 , -1, -1):
            if list_sorted[i] < list_sorted[j]:
                list_sorted[i], list_sorted[j] = list_sorted[j] , list_sorted[i]
                i = i -1
            else:
                break

    

    return list_sorted

def heap_sort(list_unsorted):
    list_sorted = []

    maxheap1=maxheap.maxheap(100)
    # build max heap from unordered array.
    maxheap1.buildMaxHeap(list_unsorted)
    for i in range(0,len(list_unsorted)):
        # swap element A[n] and A[1]. Note A[n] is the max after the swap.
        maxheap1.swap(1, maxheap1.size)
        # add A[n] to list:
        list_sorted.append(maxheap1.Heap[maxheap1.size])
        # discard node "n" by decrementing heap-size variable and setting element to zero.
        maxheap1.Heap[maxheap1.size] = 0
        maxheap1.size = maxheap1.size-1
        # new root may violate max heap, run maxheapify to fix this.
        maxheap1.maxHeapify(1)
    print(list_unsorted)
    print(list_sorted)
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
        -Tim sort.

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
    # define unsorted array.
    list1 = [5,4,6,1,3,10,52364, 12,34,1235,2]
    list2 = [1,2]

    # # apply insertion sort and print results.
    # list2 = insertion_sort(list1)
    # print(list1)
    # print("sorted list with insertion sort: " , list2)
    # print(" ")
    
    # # apply merge sort and print results.
    # print(list1)
    # merge_sort(list1, 0 , len(list1) - 1)
    # print("sorted list with merge sort: " , list1)
    heap_sort(list1)
if __name__ == "__main__":
    main()
