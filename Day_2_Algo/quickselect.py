#find the kth largest element in array

def kth(ls,k):
    ls.sort()
    return ls[len(ls) - k]





ls = [1,2,3,44,52,66,21,546,24]
print("kth largest element is ", kth(ls, 3))