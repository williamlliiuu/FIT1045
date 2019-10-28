def heapsort(lst):
    def insert(heap, item):
        heap.append(item)
        child = len(heap)-1
        parent = (child -1)//2
        while heap[child]<heap[parent] and parent>=0:
            heap[child],heap[parent] = heap[parent],heap[child]
            child = parent
            parent = (child -1)//2
    #arrange lst into heap
    def ListToHeap(lst):
        heap = []
        for i in lst:
            insert(heap, i)
        return heap
    # print(ListToHeap([3,1,5,6,1,3,5,7,0]))
    #keep extracting min
    def min_child(heap, v):
        left_child = 2*v + 1
        right_child = 2*v+2
        if left_child and right_child < len(heap):
            if heap[left_child]>heap[right_child]:
                return right_child
            else:
                return left_child
        else:
            if left_child<len(heap):
                return left_child
            elif right_child<len(heap):
                return right_child
            else:
                return -1

    def extract_min(heap):
        heap[-1],heap[0] = heap[0],heap[-1]
        root = heap.pop()
        if len(heap)>1:
            parent = 0
            swapChild = min_child(heap,parent)
            while heap[swapChild]<heap[parent] and swapChild!=-1:
                heap[parent],heap[swapChild] = heap[swapChild],heap[parent]
                parent = swapChild
                swapChild = min_child(heap, parent)
        return root

    heap = ListToHeap(lst)
    res = []
    while len(heap)>0:
        res += [extract_min(heap)]
    #return lst
    return res

# print(heapsort([1,4,1,6,74,2,3,79,3,4]))