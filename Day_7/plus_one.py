# need to add one in the last element of array

def plus_one(ls):
    ls[len(ls)-1] = ls[len(ls)-1] + 1
    return ls



ls = [0]
print(plus_one(ls))