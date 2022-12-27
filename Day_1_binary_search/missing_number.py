# find  missing number from list

def missing_number(ls):
    ls.sort()
    print(ls)
    for i in range(len(ls) -1):
        if ls[i] == 0 or ls[i]+ 1 == 0:
            continue
        elif((ls[i] + 1) != (ls[i + 1])):
            print( "missing is", ls[i] + 1)
            return 
            
    print("missing was ", ls[len(ls) -1] + 1 )
    return 

ls = [4,2,3,1,-1]
missing_number(ls)