# TO FIND THE MAJORITY OF NUMBER IN LIST OR ARRAY

def majority(ls, n):
    votes = 0
    candidate = -1

    for i in range(n):
        if (votes == 0):
            candidate = ls[i]
            votes = 1
        elif ( ls[i] == candidate):
            votes += 1
        else:
            votes -= 1
    
    count = 0

    for i in range(n):
        if (ls[i] == candidate):
            count += 1

    if (count > n // 2):
        return candidate
    else:
        return -1


ls = [1,2,3,3,3,3,4,5,6,3,3]
print("majority is ", majority(ls,len(ls)))

