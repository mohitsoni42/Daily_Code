# move all 0 to end of the list


def move_zero(ls):
    for i in range(len(ls)-1):
        if ls[i] == 0:
            temp = 0
            ls[i] = ls[i + 1]
            ls[i + 1] = temp
    return ls

ls = [0,1,2,4,5]
print(move_zero(ls))