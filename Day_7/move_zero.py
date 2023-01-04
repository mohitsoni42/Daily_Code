# move all 0 to end of the list

def move_zero(ls):
    j = 0
    for i in range(len(ls)):
        if ls[i] != 0:
            ls[j] = ls[i]
            j +=1
    
    while (j < len(ls)):
        ls[j] = 0
        j += 1

    return ls

ls =[0,0,1,2,3,0,0,4,5]
print(move_zero(ls))