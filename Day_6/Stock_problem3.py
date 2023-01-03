# we can do atmost 2 transactions

def stocks(ls):

    profit = 0
    mins = 100
    mins2 = 100
    profit2 =0
    for i in ls:
        if i < mins:
            mins = i
 
        if i - mins > profit:
                profit = i - mins
        if i- profit < mins2:
            mins2 = i- profit
        if i - mins2 > profit2:
            profit2 = i-mins2
                    
    return profit2

ls = [3,3,5,0,0,3,1,4]
print(stocks(ls))