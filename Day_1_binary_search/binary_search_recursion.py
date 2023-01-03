#same with recursion

def BS_recursion(ls, start, end, target):
    mid = (start + end) //2

    if ls[mid] == target:
        return mid +1
    elif (ls[mid] > target):
        BS_recursion(ls, start, mid -1, target)
    elif (ls[mid] < target):
        BS_recursion(ls, mid + 1, end, target)
    else:
        return -1

ls = [11,23,31,45,56,62,78,84,96]
print(BS_recursion(ls, 0, len(ls)-1, 78))