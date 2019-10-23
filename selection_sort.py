def min_index(lst): #return the index of minimum item
    min = 0
    for i in range(len(lst)):
        if lst[i] < lst[min]:
            min = i
    return min

def selection_sort(lst):
    # for all indicies i of lst:
    #     find index j of min element in sublist from i
    #     swap elements at i and j
    for i in range(len(lst)):
        j = min_index(lst[i:]) + i #index refers to slice i.e. indices of sublist start at zero therefore need to add i
        lst[i],lst[j] = lst[j],lst[i]
    return lst


