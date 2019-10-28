def partition(lst):
    pivot = lst[0]
    i = 1 #swap pos
    index = 1
    while index < len(lst):
        if lst[index] < pivot:
            lst[index],lst[i] = lst[i], lst[index]
            i+=1
        index += 1
    lst[0],lst[i-1] = lst[i-1], lst[0]

    pivotStart = i-1
    j = i
    while i < len(lst):
        if lst[i] == pivot:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        i += 1
    return (pivotStart, j)

def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivotStart, pivotEnd = partition(lst)
    pivotSection = lst[pivotStart:pivotEnd]

    sorted_left = quick_sort(lst[:pivotStart])
    sorted_right = quick_sort(lst[pivotEnd:])

    return sorted_left + pivotSection + sorted_right

# print(quick_sort([2,3,4,1,6,9,67,0,3,6,4,4,4]))