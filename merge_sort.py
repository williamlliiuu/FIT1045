def merge(l1, l2):
    res = []
    n1, n2 = len(l1), len(l2)
    i, j = 0, 0
    while i < n1 and j < n2: #while i and j is less than the length of their lists
        if l1[i]<= l2[j]:
            res += [l1[i]]
            i += 1
        else:
            res += [l2[j]]
            j += 1
    return res + l1[i:] + l2[j:]    #need to add in excess numbers if len of lists are different

def merge_sort(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return lst
    else:
        mid = len(lst)//2
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

# print(merge_sort([1,5,63,1,-2,9]))


