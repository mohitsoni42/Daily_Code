

def smalle(ls):
    min1 = 100
    min2 = 100

    for i in range(len(ls)):
        if ls[i] < min1:
            min1 = ls[i]
        
        if (ls[i] < min2) > min1:
            min2 = ls[i]

    print (min1, min2)


a = [-19, -1, -5, 2, 5, 8, 10, 14, -18]
print(smalle(a))
