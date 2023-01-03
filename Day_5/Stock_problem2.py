# we need to find the max profit, we are allowed to do many transactions

def max_profit(ls):
    profit = 0

    for i in range(1, len(ls) ):
        if (ls[i] > ls[i -1]):
            profit += ls[i]- ls[i -1]
    
    return profit

ls = [7,1,5,3,6,4]

print(max_profit(ls)) 