def binary_search(v, seq):
    a = 0
    b = len(seq) - 1
    while a <= b:
        mid = (a+b)//2
        if v == seq[mid]:
            return mid
        elif v < seq[mid]:
            b = mid -1
        else:
            a = mid + 1
    return None
