# if elements occurs half the size of array then it is majority element

def majority(ls):
    candidate = 0
    votes = 0

    for i in ls:
        if votes == 0:
            candidate = i
        if i == i +1:
            votes += 1
        else:
            votes -= 1

    count =0

    for i in ls:
        if i == candidate:
            count += 1
    
    if count > len(ls)//2:
        return candidate
    
    return -1


ls = [3,2,3]
print(majority(ls))