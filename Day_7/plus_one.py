# need to add one in the last element of array

#first approach
def plus_one(ls):

    if ls[len(ls)-1] == 9:
        ls[len(ls)-1] = 0
        ls[len(ls)-2] = ls[len(ls)-2] + 1
    else:
        ls[len(ls)-1] = ls[len(ls)-1] + 1
    return ls



# better approach

def plus_one_better(ls):

    for i in range(len(ls)-1,-1,-1) :
        if ls[i] < 9:
            ls[i] +=1
            return ls
        else:
            ls[i] = 0
    ls[0] = 1
    ls.append(0)
    return ls

ls = [1,9,9]
ls2= [9,9,9]
print(plus_one(ls))

print(plus_one_better(ls2))