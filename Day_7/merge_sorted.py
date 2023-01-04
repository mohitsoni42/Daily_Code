#array question


def merge_array(ls, ls2):

    j = 0

    for i,v in enumerate(ls):
        if ls[i] <= ls2[i]:
            ls[i] = ls[i]
        else:
            ls[i] = ls2[i]
    return ls

ls = [1,5,7,0,0,0]
ls2 = [8,2,6]

print(merge_array(ls,ls2))