#find the peak index of mountain array
# find the index of max element

def peak_index(ls):
    maxs = -100
    for i in range(len(ls)):
        if ls[i] > maxs:
            maxs = ls[i]
            index  = i

    return index


ls = [0,2,1,0]
print(peak_index(ls))