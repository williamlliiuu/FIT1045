def is_attacked(row, col, partial):
    #if any of queens in partial attack the next possible position, return true
    for i in range(len(partial)):
        if row == partial[i] or col == i or abs(row-partial[i]) == abs(col - i):
            return True
    return False

def options(partial, n):
    opts = []
    nextCol = len(partial)  #next column to insert at
    for i in range(n):  #look at every row
        if not is_attacked(i, nextCol, partial):    #if proposed position is not attacked by any queens on board
            opts += [i]
    return opts
# print(options([0,2],8))

def queens(n, part = []):
    if len(part)==n:    #if we placed n numbers of queens, return the configuration
        return [part]
    else:   #for each augmentation of current partial, augment the augmentation of current and add to result
        res = []
        for o in options(part,n):
            res += queens(n, part + [o])
        return res

# print(queens(4))
