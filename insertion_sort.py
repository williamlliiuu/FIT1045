def insert(k,lst):
    """
    accepts: list lst of length n>k>=0 of comp. elements such that lst[:k-1] is sorted
    postcon: lst[:k] is sorted
    """
    j = k
    while j > 0 and lst[j-1]>lst[j]:
        lst[j-1],lst[j] = lst[j],lst[j-1]
        j = j-1

def insertion_sort(lst):
    """
    accepts: list lst of length n of comparable elements
    post-cond: lst has same elements as on call but sorted in ascending order
    """

    for i in range(1,len(lst)):
        insert(i,lst)
    return lst

# print(insertion_sort([-2,-4,4,5,1,3]))

