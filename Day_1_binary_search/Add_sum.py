# sum of 2 numbers should be k
def target_sum(k, ls):
    for i in range(len(ls)) :
        if (k- ls[i]) in ls:
            print("2 numbers will add up to k")
            return 0 
    
    print("Noope")
    return -1

ls = [12,23,34,45,56,6,77,889,2,5]
target_sum(13, ls)
